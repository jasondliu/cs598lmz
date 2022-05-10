import mmap
# Test mmap.mmap()
path = 'large_file'
mf = open(path, 'r+b')
offset = 0
size = len(mf)
map = mmap.mmap(mf.fileno(), size)
mmap.ACCESS_READ()
mmap.ACCESS_COPY()
mmap.ACCESS_WRITE()
mmap.ACCESS_DEFAULT()
