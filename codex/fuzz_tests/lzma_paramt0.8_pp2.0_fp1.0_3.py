from lzma import LZMADecompressor
LZMADecompressor().decompress(pack)

# --------------------------------------
# function to combine the two files
# returns the complete file
def combined(path1, path2):
    with open(path1) as file1:
        file1_string = file1.read()
    with open(path2) as file2:
        file2_string = file2.read()
    return file1_string + file2_string

combined(path1, path2)
# --------------------------------------

# --------------------------------------
# function to create a text file
# takes two strings and writes them to the file
def create(path1, path2):
    with open(path1) as file1:
        file1_string = file1.read()
    with open(path2) as file2:
        file2_string = file2.read()
    with open('new_file_name.txt', 'w') as new_file:
        new_file.write(file1_string)
        new_file.write(file2_string)

create(path1, path2)
# --------------------------------------


