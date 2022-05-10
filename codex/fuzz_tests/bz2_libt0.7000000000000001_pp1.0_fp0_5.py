import bz2
bz2.BZ2File(path).readline()

# Reading text files line by line
#
# with open('somefile.txt') as f:
#     for line in f:
#         ... process line ...

# Example of Reading Binary Data Record 
#
# with open('data.pk', 'rb') as f:
#     data = pickle.load(f)

# Writing Text to a File
with open('test.txt', 'w') as f:
    f.write('Hello\n')
    f.write('World\n')

# Writing Binary Data to a File
with open('test.bin', 'wb') as f:
    f.write(b'Hello\n')
    f.write(b'World\n')

# print(f.closed)

# Problem
#
# You have data in a sequence of strings or bytes and you want to write it to a file.
#
# Solution
#
# The built-in function open() creates a Python file object, which serves as a link to a file residing on your machine.
#
#
