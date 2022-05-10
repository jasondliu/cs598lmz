import mmap
# Test mmap.mmap()

size = 1024

with open('./test.txt', 'r+') as f:
    mm = mmap.mmap(f.fileno(), size)
    mm.seek(size+1)
    mm.write(b'a')
