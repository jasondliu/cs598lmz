import bz2
bz2.open(filename, mode='rt', encoding='utf-8', errors='replace')
# mode='rt' stands for 'read text'

# bz2.open() can accept a variety of parameters, including the encoding and errors parameters that we saw in Chapter 7.

# open() will return a file-like object, so we can iterate over the lines of the file as follows:

# filename = 'example.bz2'
# with bz2.open(filename, 'rt') as f:
#     for line in f:
#         print(line)

# We can also use the read() method to read the entire file at once:

# with bz2.open(filename, 'rt') as f:
#     file_content = f.read()
#     print(file_content)

# The file-like object returned by bz2.open() also has a write() method, which we can use to compress data in real time.
# We can do this by passing mode='wt' to bz2.open():

# with bz2.open(filename, 'wt
