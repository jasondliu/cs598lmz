import mmap
# Test mmap.mmap() with a non-zero offset and a length larger than the file size
with open(tmpfile, 'w') as fp:
    fp.write('a')
with open(tmpfile, 'r+b') as fp:
    m = mmap.mmap(fp.fileno(), 10, offset=1)
