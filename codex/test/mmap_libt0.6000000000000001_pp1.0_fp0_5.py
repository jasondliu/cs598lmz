import mmap

# open the file in readonly mode
f = open('test.txt', 'r')

# memory-map the file, size 0 means whole file
