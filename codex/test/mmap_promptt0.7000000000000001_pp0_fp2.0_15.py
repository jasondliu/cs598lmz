import mmap
# Test mmap.mmap 
buffer = mmap.mmap(-1, 4096)

buffer[:len(message)] = message
buffer.seek(0)

buffer.write(b'O_O\n')
print('Before:', buffer.readline())
buffer.seek(0)
print('After :', buffer.readline())
