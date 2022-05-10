import mmap
# Test mmap.mmap size = 0
with open('test.txt', 'w+') as f:
    f.write('1' * 1024 * 1024)
