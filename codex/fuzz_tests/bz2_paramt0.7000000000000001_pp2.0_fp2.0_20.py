from bz2 import BZ2Decompressor
BZ2Decompressor()

import gzip
gzip.open(filename, mode='rt')

import lzma
lzma.open(filename)

# Reading text files line by line
# f = open(filename, encoding='utf-8')
# for line in f:
#     print(line)

# Reading text files line by line
# f = open(filename, encoding='utf-8')
# lines = f.readlines()

# Reading text files line by line
# f = open(filename, encoding='utf-8')
# lines = list(f)

# Reading text files line by line
# f = open(filename, encoding='utf-8')
# lines = f.read().splitlines()

# Reading binary files in chunks
# with open(filename, 'rb') as f:
#     size = 1024
#     data = f.read(size)
#     while data:
#         process(data)
#         data = f.read(size)

# Writing text files
# with open(filename, 'wt', encoding='utf-8') as f:
#
