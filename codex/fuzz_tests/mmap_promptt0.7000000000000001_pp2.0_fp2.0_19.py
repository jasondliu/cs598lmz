import mmap
# Test mmap.mmap size = 0
with open('test.txt', 'w+') as f:
    f.write('1' * 1024 * 1024)
with open('test.txt', 'r') as f:
    mm = mmap.mmap(f.fileno(), 0)
    mm.size() # should return 1024 * 1024
</code>

