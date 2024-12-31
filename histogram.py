# ECOR 1042 Lab 6 - Individual submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Caroline Twelves"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101301400"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-098"

#==========================================#
# Place your histogram function after this line
import matplotlib.pyplot as plt


def histogram(data: list[dict], attribute: str) -> int:
    """ This function will print a histogram of the attibutes from the dictionarys in the list, to display how many of each type there are. If it is a cotegorial attribute the function will return -1, else it will return the highest attribute
    Preconditions: machine_dicts[all][key_to_plot] (key_to_plot is a key in all dicts in the list

    >>> histogram([{'hi': 1}, {'hi': 2}, {'hi': 3}, {
    'hi': 4}, {'hi': 3}, {'hi': 1}], 'hi')
    4
    >>> histogram([{'some_attribute': 'pi', 'hi': 2}, {'hi': 3,
    'some_attribute': 'pi'}, {'some_attribute': 'leos_is_the_best', 'hi': 1}], 'some_attribute')
    -1
    >>> histogram([{'1042': 1}, {'1042': 1}, {'1042': 1}, {'1042': 1}], '1042')
    1
    """
    # variables that shall be used throughout the function
    list_items = []
    number_of_copys = {}
    index = 0

    # take all items tied to key given and put them into a list
    for element in range(len(data)):
        list_items.append(data[element][attribute])

    # count all duplicates
    while len(list_items) > 0:

        index = 0
        # append the key with item of 1 to the list
        number_of_copys[list_items[0]] = 1

        # loop through all items to find matches
        for i in range(len(list_items)):
            # check for a martch but not with itself
            if 0 != index and list_items[0] == list_items[index]:
                # add count to dict of list_items[0] in number_of_copys
                number_of_copys[list_items[0]] += 1
                # del the index so its only recorded once
                del list_items[index]
                index -= 1
            index += 1

        # del the original becuase it and all its duplicates should have been recorded
        del list_items[0]

    # put keys and values into their own lists
    items_x = list(number_of_copys.keys())
    count_y = list(number_of_copys.values())

    # set and display histogram (bar graph)
    fig1 = plt.figure()
    plt.title("Simple Bar")
    plt.xlabel(attribute + ' attribute')
    plt.ylabel('Amount of ' + attribute + "'s")
    plt.bar(items_x, count_y, color='cyan')
    plt.show()

    # return max int if attributes are ints, if not, return -1
    if type(items_x[0]) == int:
        return max(items_x)
    else:
        return -1


# Do NOT include a main script in your submission
