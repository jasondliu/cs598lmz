import mmap
# Test mmap.mmap()

# memory-map a file, size 0 means whole file
m = mmap.mmap(f.fileno(), 0)
# read content via standard file methods
print(m.readline())  # b'This is the first line of the file.\n'
# read content directly from the memory-mapped file
print(m[0:11])  # b'This is the f'
# update content using standard file methods
m.seek(0)  # rewind
m.write(b'That is the first line.')
# update content directly, (word size-1) bytes long
m[11:22] = b'first line of'
# ...
# close the map
m.close()

# memory-map an *anonymous* memory block, size 0 means whole block
m = mmap.mmap(-1, 0)
# ...
# close the map
m.close()
