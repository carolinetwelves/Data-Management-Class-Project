# ECOR 1042 Lab 6 - Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = ""

# Update "" with your student number (e.g., 100100100)
__student_number__ = ""

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = ""


# ==========================================#
# Place your script for your batch_UI after this line
import load_data
import curve_fit
import sort
import histogram

# Define the command codes
LOAD_COMMAND = 'L'
FILTER_COMMAND = 'F'
SORT_COMMAND = 'S'
HISTOGRAM_COMMAND = 'H'

# Ask the user for the name of the command file
filename = input('enter name of the file: ')

# Open the command file and execute each command
with open(filename) as f:
    for line in f:
        # Parse the command from the line
        command_parts = line.strip().split(';')
        command_code = command_parts[0]
        command_args = command_parts[1:]

        # Execute the command based on its code
        if command_code == LOAD_COMMAND:
            load_data.load_data(command_parts[1], (command_parts[2], command_parts[3]))
            print('Data loaded')
        elif command_code == FILTER_COMMAND:
            curve_fit.curve_fit(*command_args)
        elif command_code == SORT_COMMAND:
            sort.sort_data(*command_args)
            print('Data sorted. ')
        elif command_code == HISTOGRAM_COMMAND:
            histogram.histogram(*command_args)
        else:
            print("")
