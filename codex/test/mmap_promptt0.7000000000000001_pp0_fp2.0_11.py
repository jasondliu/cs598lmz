import mmap
# Test mmap.mmap
with open('/dev/urandom', 'r+b') as f:
    f.seek(0, os.SEEK_END)
    fsize = f.tell()
    f.seek(0, os.SEEK_SET)
    mappable = mmap.mmap(f.fileno(), fsize)

# Test mmap.mmap with a small offset
with open('/dev/urandom', 'r+b') as f:
    mappable = mmap.mmap(f.fileno(), 0, offset=1000)
