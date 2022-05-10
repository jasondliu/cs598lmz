import mmap
# Test mmap.mmap()

'''
This is a test to see how to open a file using mmap.mmap. This allows the file to be
treated as both a file and a sequence of bytes. We can edit the bytes.

'''

file = open('test.txt', 'r+')
#memory-mapping the file, size 0 means whole file
map_file = mmap.mmap(file.fileno(), 0)

#print the file
print (map_file[:])

#Replace the first 10 characters with <><> (mmap treats the file as a sequence of bytes)
map_file.seek(0)
map_file.write('<><><><><><><><>')

#print the file again
print (map_file[:])

#close the file
map_file.close()
