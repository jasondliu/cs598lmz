import mmap
# Test mmap.mmap using a file
with open('test.txt', 'r') as f:
    arr = mmap.mmap(f.fileno(), 0, access=mmap.ACCESS_READ)
    print ('Before modification:', arr.readline().rstrip())

    # Move to the beginning of the file
    arr.seek(0)
    # Write the new line at the beginning of the file
    arr.write(b'This is a TEST')

    arr.seek(0)
    print ('After modification:', arr.readline().rstrip())

# Test mmap.mmap creating the memory map directly from bytes
print ('From bytes:', mmap.mmap(-1, 13).write(b'Hello World!\n').readline())

# Test mmap.mmap directly creating the memory map from a bytes object
print ('From bytes object:', mmap.mmap().write_byte(ord('H')).write_byte(ord('e')).write_byte(ord('l')).write_byte(ord('l')).write_byte(ord('o')).readline())

