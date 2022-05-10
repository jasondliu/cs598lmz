import mmap
# Test mmap.mmap()

filename = "python_mmap_test"
size = 100

with open(filename, 'wb') as f:
    f.seek(size - 1)
    f.write(b'\0')

with open(filename, 'r+') as f:
    m = mmap.mmap(f.fileno(), size)
    m[0:size] = b'1' * size
    m.seek(0)
    print(m.readline())
    m.close()

os.remove(filename)

# Test mmap.mmap() using file-like object

class FileLike:
    def read(self, size):
        return b'\0' * size
    def write(self, data):
        pass

m = mmap.mmap(-1, size, access=mmap.ACCESS_WRITE)
m[0:size] = b'1' * size
m.seek(0)
print(m.readline())
m.close()

