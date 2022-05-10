import bz2
bz2.BZ2File(filename)

# How to read a file line by line
def read_file_line_by_line(filename):
    with open(filename) as f:
        for line in f:
            print(line)

# How to read a file line by line and store it in a list
def read_file_line_by_line_and_store_in_list(filename):
    with open(filename) as f:
        return [line.rstrip() for line in f]

# How to read a file and store it in a list
def read_file_and_store_in_list(filename):
    with open(filename) as f:
        return f.read().splitlines()

# How to read a file and store it in a list (faster)
def read_file_and_store_in_list_faster(filename):
    with open(filename) as f:
        return list(f)

# How to read a file and store it in a dictionary
def read_file_and_store_in_dictionary(filename):

