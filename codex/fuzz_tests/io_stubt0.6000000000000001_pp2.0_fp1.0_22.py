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
gc.collect()
print(view)
print('#'*20)

# A BufferedReader can be used with a file object that doesn't even have a readinto method
class File:
    def __init__(self):
        self.closed = False
    def read(self, size):
        return b'x' * size

f = io.BufferedReader(File())
print(f.read(5))
f.close()
print('#'*20)

# A BufferedReader can be used with a file object that doesn't even have a read method
class File:
    def __init__(self):
        self.closed = False
    def readinto(self, buf):
        buf[:] = b'x' * len(buf)

f = io.BufferedReader(File())
print(f.read(5))
f.close()
print('#'*20)

# Test that the garbage collector handles cycles
class File:
    def __init__(self):
        self.closed = False
        self.buf = io.BytesIO(
