# ECOR 1042 Lab 5 - Team submission
# Remember to include docstring and type annotations for your functions

# Update "" to list all students contributing to the team work
__author__ = "RILEY HANNA, CAROLINE TWELVES, ADAM LOFARO, MARYAM ALSHAWAFI"

# Update "" with your team (e.g. T102)
__team__ = "T098"


# ==========================================#
# Place your sort_cache_bubble function after this line
def sort_cache_bubble(list_dicts: list[dict], sorted_order: str) -> list[dict]:
    """ The function returns the sorted lists of dictionarys by acending ("A") or descending ("D") order relative to the CASH attribute. If there is no CACH key, an error message will be displayed.
    Preconditions: sorted_order == "A" or sorted_order == "D"

    >>> sort_cache_bubble([{"CACH":20,"Model":"GP"},{"CACH":19,"Model":"MS"},{"CACH":14,"Model":"MS"}], "D")
    [{'CACH': 20, 'Model': 'GP'}, {'CACH': 19, 'Model': 'MS'}, {'CACH': 14, 'Model': 'MS'}]
    >>> sort_cache_bubble([{"CACH":3,"Model":"GP"},{"CACH":64,"Model":"MS"},{"CACH":15,"Model":"MS"}], "A")
    [{'CACH': 3, 'Model': 'GP'}, {'CACH': 15, 'Model': 'MS'}, {'CACH': 64, 'Model': 'MS'}]
    >>> sort_cache_bubble([{"CACH":3,"Model":"GP"},{"CACH":64,"Model":"MS"},{"NOTCACH":15,"Model":"MS"}], "A")
    "CACH" key is not present in at least one dictionary
    [{'CACH': 3, 'Model': 'GP'}, {'CACH': 64, 'Model': 'MS'}, {'NOTCACH': 15, 'Model': 'MS'}]
    """

    # to sort in ascending or descending order
    if sorted_order == 'A':
        ascending = 1
        descending = 0
    else:
        ascending = 0
        descending = 1

    cach_items = []  # get and sort items from the list of key 'CACH'
    original_order = []  # keep record of original index of sorted items
    sorted_order = []  # sort all dicts from original list

    # get all items with key "CACH" from list
    for element in range(len(list_dicts)):
        try:
            cach_items.append(list_dicts[element]["CACH"])
            original_order.append(element)
        except:
            print('"CACH" key is not present in at least one dictionary')
            return list_dicts

    # bubble sort
    swap = True
    while swap:
        swap = False
        for bubble in range(len(cach_items) - 1):

            # if the item is bigger/ smaller (acending/descending) than the last
            if cach_items[bubble + descending] > cach_items[bubble + ascending]:
                # swap items and keep track or original order
                cach_items[bubble], cach_items[bubble
                                               + 1] = cach_items[bubble + 1], cach_items[bubble]
                original_order[bubble], original_order[bubble +
                                                       1] = original_order[bubble + 1], original_order[bubble]
                swap = True

    # add original list of dicts in order sorted
    for element in range(len(cach_items)):
        sorted_order.append(list_dicts[original_order[element]])
    return sorted_order  # return sorted list


# ==========================================#
# Place your sort_prp_selection function after this line
def sort_prp_selection(machines, order):
    """
    The purpose of sort_prp_selection() is to sort using the selection sort algorithm. Taking two paramaters, the machine
    list, and the ascending or descending order, the function returns the appropriate list.

    Examples:
    >>> sort_prp_selection([{"PRP":10,"Model":"GP"}, {"PRP":19,"Model":"MS"}], "D")
    [{'PRP': 19, 'Model': 'MS'}, {'PRP': 10, 'Model': 'GP'}]
    >>> sort_prp_selection([{"Model":"GP"},{"Model":"MS"}], "D")
    "PRP" key is not present
    [{'Model': 'GP'}, {'Model': 'MS'}]
    >>> sort_prp_selection([{"PRP":10,"Model":"GP"}, {"PRP":19,"Model":"MS"}], "A")
    [{'PRP': 10, 'Model': 'GP'}, {'PRP': 19, 'Model': 'MS'}]
    """
    if not machines:
        return machines

    prp_key = "PRP"

    if not machines[0].get(prp_key):
        print(f'"{prp_key}" key is not present')
        return machines

    for i in range(len(machines) - 1):
        min_max_index = i
        for j in range(i + 1, len(machines)):
            if machines[j].get(prp_key) is not None:
                if order == "A" and machines[j][prp_key] < machines[min_max_index][prp_key]:
                    min_max_index = j
                elif order == "D" and machines[j][prp_key] > machines[min_max_index][prp_key]:
                    min_max_index = j

        machines[i], machines[min_max_index] = machines[min_max_index], machines[i]

    return machines


# ==========================================#
# Place your sort_m_avg_insertion function after this line
def sort_m_avg_insertion(file: list[dict], choice: str) -> list[dict]:
    if not all('M_AVG' in machine for machine in file):
        print('M_AVG key is not present')
        return file

    else:
        for i in range(1, len(file)):
            value = file[i]
            j = i - 1
            key = file[i]['M_AVG']

            while j >= 0 and (file[j]['M_AVG'] > key):
                file[j + 1] = file[j]
                j -= 1
            file[j + 1] = value  # {'M_AVG': key, 'MODEL': file[i]['MODEL']}

        if choice == 'D':
            file.reverse()

        return file


# ==========================================#
# Place your sort_myct_bubble function after this line
def sort_myct_bubble(machine_list, order):
    """
    The purpose of sort_myct_bubble() is to sort using the bubble sort algorithm, taking two paramaters, the machine
    list, as well as ascending or descending order.

    Examples:
    >>> sort_myct_bubble([{"MYCT":10,"Model":"GP"},{"MYCT":19,"Model":"MS"}], "D")
    [{'MYCT': 19, 'Model': 'MS'}, {'MYCT': 10, 'Model': 'GP'}]
    >>> sort_myct_bubble([{"Model":"GP"}, {"Model":"MS"}], "D")
    "MYCT" key is not present.
    [{'Model': 'GP'}, {'Model': 'MS'}]
    >>> sort_myct_bubble([{"MYCT":10,"Model":"GP"},{"MYCT":19,"Model":"MS"}], "A")
    [{'MYCT': 10, 'Model': 'GP'}, {'MYCT': 19, 'Model': 'MS'}]
    """
    # Check if "MYCT" is present
    if not machine_list or not machine_list[0].get("MYCT"):
        print('"MYCT" key is not present.')
        return machine_list

    # For loop with bubble sort algorithm.
    for i in range(len(machine_list) - 1):
        for j in range(0, len(machine_list) - i - 1):
            # Check if ascending or descending input is valid, then swap
            if order == "A":
                if machine_list[j]["MYCT"] > machine_list[j + 1]["MYCT"]:
                    machine_list[j], machine_list[j + 1] = machine_list[j + 1], machine_list[j]
            elif order == "D":
                if machine_list[j]["MYCT"] < machine_list[j + 1]["MYCT"]:
                    machine_list[j], machine_list[j + 1] = machine_list[j + 1], machine_list[j]

    return machine_list


# ==========================================#
# Place your sort function after this line
def sort(input: list[dict], choice: str, by: str) -> list[dict]:
    if by == 'CACH':
        return sort_cache_bubble(input, choice)
    if by == 'PRP':
        return sort_prp_selection(input, choice)
    if by == 'M_AVG':
        return sort_m_avg_insertion(input, choice)
    if by == 'MYCT':
        return sort_myct_bubble(input, choice)
    return input

# Do NOT include a main script in your submission
