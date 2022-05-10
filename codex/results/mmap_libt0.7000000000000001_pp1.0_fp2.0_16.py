import mmap
import re

# file = open('file.txt', 'r+')
# size = os.path.getsize('file.txt')

# create a memory map in read-write mode
# m = mmap.mmap(file.fileno(), size, access=mmap.ACCESS_WRITE)

# read the contents of a file
# print(m.readline())

# print(os.path.getsize('file.txt'))
# print(os.path.getsize('file1.txt'))

# open files
f1 = open('file1.txt', 'r+')
f2 = open('file2.txt', 'r+')

# get file sizes
size1 = os.path.getsize('file1.txt')
size2 = os.path.getsize('file2.txt')

# create memory maps
m1 = mmap.mmap(f1.fileno(), size1, access=mmap.ACCESS_WRITE)
m2 = mmap.mmap(f2.fileno(), size2, access=
