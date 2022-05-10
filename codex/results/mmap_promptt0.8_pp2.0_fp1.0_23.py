import mmap
# Test mmap.mmap.tell
with open('test.txt', 'r+b') as fp:
    map = mmap.mmap(fp.fileno(), 0)
    print(map.tell(), map.seek(0, 1))
