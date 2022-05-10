import mmap
# Test mmap.mmap with file
fname = "ma.txt"
print(os.path.getsize(fname))
f = open(fname, 'r+')
map_file = mmap.mmap(f.fileno(), os.path.getsize(fname), access=mmap.ACCESS_READ)
for i in range(1000000):
    map_file.seek(i)
    print(map_file.read(1))
f.close()
# Test mmap.mmap with bytearray
ba = bytearray(os.path.getsize(fname))
with open(fname, 'rb') as f:
    ba[:] = f.read()
map_byte = mmap.mmap(-1, len(ba), access=mmap.ACCESS_READ)
map_byte.move(ba.buffer_info()[0], 0)
for i in range(1000000):
    map_byte.seek(i)
    print(map_byte.read(1))
# Test mmap.mmap with bytearray
