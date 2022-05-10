import mmap
# Test mmap.mmap

print(mmap.HAVE_SYNC)
print(mmap.PAGESIZE)

mm = mmap.mmap(-1, 1024)
mm.write(b"test")
mm.read(4)
print(mm.size())
mm.close()
# Test mmap.mmap() with fileno and access

sample = b' '*1024

with open('map_file.txt', 'w+b') as f:
    f.write(sample)

with open('map_file.txt', 'r+b') as f:
    print(mmap.mmap(f.fileno(), 1024, access=mmap.ACCESS_COPY).read(1024))

os.unlink('map_file.txt')
# Test mmap.mmap() with fileno initial value

sample = b' '*1024

with open('map_file.txt', 'w+b') as f:
    f.write(sample)

with open('map_file.txt', 'r+b') as f:
    print(mmap
