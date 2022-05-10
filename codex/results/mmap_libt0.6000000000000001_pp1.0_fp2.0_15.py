import mmap

def load_data(file_name):
    """
    This function reads the data from the file and returns the data in a single string
    """
    with open(file_name, "rb") as f:
        content = f.read()
    return content

def get_data_list(data_string):
    """
    This function parses the data into a list of integers
    """
    return [int(x) for x in data_string.split(",")]

def get_meta_data(data_list):
    """
    This function returns a tuple (puzzle_input, puzzle_input_backup)
    """
    puzzle_input = data_list.copy()
    puzzle_input_backup = data_list.copy()
    return (puzzle_input, puzzle_input_backup)

def get_opcode(puzzle_input):
    """
    This function calculates the opcode
    """
    return puzzle_input % 100

def get_parameters(puzzle_input, puzzle_input_backup, position):
    """
