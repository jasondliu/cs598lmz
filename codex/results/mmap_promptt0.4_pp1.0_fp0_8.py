import mmap
# Test mmap.mmap(fileno, length)
#
# 1. Test when length is 0.
# 2. Test when length is non-zero, but smaller than the size of the file.
# 3. Test when length is equal to the size of the file.
# 4. Test when length is larger than the size of the file.

# 1. Test when length is 0.
with open('mmap_file_1', 'w+b') as f:
    f.write(b'abcdefghijklmnopqrstuvwxyz')
    mm = mmap.mmap(f.fileno(), 0)
    assert mm.read(1) == b'a'
    assert mm.read(1) == b'b'
    assert mm.read(1) == b'c'
    mm.close()

# 2. Test when length is non-zero, but smaller than the size of the file.
with open('mmap_file_2', 'w+b') as f:
    f.write(b'abcdefghijklmnopqrstuvwxyz')
   
