from read_packages import read_file
file_path_local = "./enem_list.txt"

import sys

def process_arguments():
    # Check if the correct number of arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script.py <argument>")
        sys.exit(1)
    if len(sys.argv[1]) != 2:
        print("only 'in' and 'un' parameter supported")
        sys.exit(1)
    if sys.argv[1] != 'in' and sys.argv[1] != 'un':
        print("only 'in' and 'un' parameter supported")
        sys.exit(1)
    # Retrieve the argument from the command line
    argument = sys.argv[1]
    # Your script logic based on the argument
    read_file(file_path= file_path_local, option = argument)

# Call the function to process arguments
process_arguments()
