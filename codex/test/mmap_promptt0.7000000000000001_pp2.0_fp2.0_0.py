import mmap
# Test mmap.mmap(fileno,length,flags)
# Make sure input file is at least 1024 bytes long.
f = open('test.txt','r')
