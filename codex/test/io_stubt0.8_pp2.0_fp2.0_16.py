import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
print(view[0])

# Test basic properties of readinto()
# Test that the argument is a writable buffer.
readinto_ranges = [(0, 3), (1, 5), (6, 9), (3, 6)]
for n in (-1, 0, 1, 2, 10, 200, 2000):
    for start, stop in readinto_ranges:
        f = io.BufferedReader(File())
