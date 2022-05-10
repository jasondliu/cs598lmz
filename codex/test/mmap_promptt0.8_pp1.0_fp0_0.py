import mmap
# Test mmap.mmap.write
import mmap

m = mmap.mmap(-1, 1)
m.write(b"x")
m.seek(0)
print(m.read().decode())
m.close()
import mmap
# Test mmap.mmap.seek_read
import mmap

m = mmap.mmap(-1, 1)
m.write(b"x")

try:
    m.seek_read(0, 1, [1])
except ValueError:
    print("ValueError")

m.seek(0)
print(m.read().decode())
m.close()
import mmap
# Test mmap.mmap.seek_write
import mmap

m = mmap.mmap(-1, 1)
m.write(b"x")

try:
    m.seek_write(0, 1, [1])
except ValueError:
    print("ValueError")

m.seek(0)
print(m.read().decode())
m.close()
import mmap
