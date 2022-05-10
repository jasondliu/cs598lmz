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

# The buffer should be cleared when the file is closed
assert view[0] == 0

# Issue #10: io.BufferedReader.readinto() should work with
# non-writable buffers
f = io.BufferedReader(File())
b = memoryview(bytearray(1))
f.readinto(b)
assert b[0] == 0

# Issue #10: io.BufferedReader.readinto() should work with
# read-only buffers
f = io.BufferedReader(File())
b = memoryview(bytes(1))
f.readinto(b)
assert b[0] == 0

# Issue #10: io.BufferedReader.readinto() should work with
# non-writable buffers
f = io.BufferedReader(File())
b = memoryview(bytearray(1))
f.readinto(b)
assert b[0] == 0

# Issue #10: io.BufferedReader.readinto() should work with
# read-only buffers
f = io.BufferedReader(File())
b = memory
