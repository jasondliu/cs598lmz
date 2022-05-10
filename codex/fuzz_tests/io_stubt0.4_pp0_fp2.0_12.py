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
print(view)

# Test that a BufferedReader can be used as a context manager.
with io.BufferedReader(io.BytesIO(b"abc")) as f:
    print(f.read(1))

# Test that a BufferedReader can be used as a context manager.
with io.BufferedReader(io.BytesIO(b"abc")) as f:
    print(f.read(1))

# Test that a BufferedReader can be used as a context manager.
with io.BufferedReader(io.BytesIO(b"abc")) as f:
    print(f.read(1))

# Test that a BufferedReader can be used as a context manager.
with io.BufferedReader(io.BytesIO(b"abc")) as f:
    print(f.read(1))

# Test that a BufferedReader can be used as a context manager.
with io.BufferedReader(io.BytesIO(b"abc")) as f:
    print(f.read(1))

# Test that a BufferedReader can be used as a context
