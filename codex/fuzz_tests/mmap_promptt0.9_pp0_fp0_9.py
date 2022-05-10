import mmap
# Test mmap.mmap object by setting element.
with open('data.bin', 'r') as f:
    size = os.fstat(f.fileno()).st_size
    # f.seek(size - 1)
    f.seek(0)
    m = mmap.mmap(f.fileno(), size, access=mmap.ACCESS_READ)
    m[0] = 255
    # m[size - 1] = 255
    m.close()
 
# Test numpy array.
a = np.memmap('data.bin', dtype=np.uint8, mode='r', shape=(1, 512))
# a[0][0] = 255
a[0][511] = 255
del a

# Test python's mutable bytes.
with open('data.bin', 'r+b') as f:
    f.seek(0)
    s = memoryview(f.read())
    print(s[0], s[511])
    # s[0] = 255
    s[511] = 255
s = memoryview(open('data.bin',
