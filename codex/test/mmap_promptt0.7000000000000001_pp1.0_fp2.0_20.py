import mmap
# Test mmap.mmap size
f = open('data.txt', 'w+')
f.write('\x00' * mmap.PAGESIZE * 2)
f.close()

f = open('data.txt', 'r+')
m = mmap.mmap(f.fileno(), 0)
