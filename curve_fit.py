# ECOR 1042 Lab 6 - Individual submission for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "MARYAM ALSHAWAFI"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101209796"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T098"


# ==========================================#
# Place your curve_fit function after this line
def curve_fit(data_list, attribute, degree):
    # Create a dictionary to store the average 'M_AVG' for each attribute level
    avg_values = {}

    # Iterate through the list of dictionaries
    for entry in data_list:

        attr_value = entry[attribute]
        m_avg = entry['M_AVG']

        if attr_value not in avg_values:
            avg_values[attr_value] = []

        # Append 'M_AVG' to the corresponding attribute level
        avg_values[attr_value].append(m_avg)

    # Calculate the average 'M_AVG' for each attribute level
    for attr_value, m_avg_list in avg_values.items():
        avg_values[attr_value] = sum(m_avg_list) / len(m_avg_list)

    # Check if the number of data points is less than the degree
    if len(avg_values) < degree:
        degree = len(avg_values) - 1

    x_data = list(avg_values.keys())
    y_data = list(avg_values.values())

    n = degree + 1  # number of coefficients
    A = [[sum(x_i ** (i + j) for x_i in x_data) for j in range(n)] for i in range(n)]
    B = [sum(x_i ** i * y_i for x_i, y_i in zip(x_data, y_data)) for i in range(n)]

    for i in range(n):
        pivot = A[i][i]

        for j in range(i + 1, n):
            factor = A[j][i] / pivot

            for k in range(i, n):
                A[j][k] -= factor * A[i][k]

            B[j] -= factor * B[i]

    coefficients = [0] * n

    for i in range(n - 1, -1, -1):
        coefficients[i] = B[i] / A[i][i]

        for j in range(i - 1, -1, -1):
            B[j] -= A[j][i] * coefficients[i]

    # Generate the equation string for the best fit
    equation = "y = "
    for i in range(degree, 0, -1):
        equation += f"{coefficients[i]}x^{i} + "
    equation += str(coefficients[0])

    return equation

# Do NOT include a main script in your submission
