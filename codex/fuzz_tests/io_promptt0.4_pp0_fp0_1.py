import io
# Test io.RawIOBase.readall()

# Test that readall() returns a bytes object.
# Test that readall() reads the entire contents of the file.
# Test that readall() does not read past the end of the file.
# Test that readall() does not change the file position.
# Test that readall() is not affected by a previous seek() call.

# Test that readall() returns a bytes object.
class ReadallBytes(io.RawIOBase):
    def read(self, n=-1):
        return b"test"

r = ReadallBytes()
assert r.readall() == b"test"

# Test that readall() reads the entire contents of the file.
class ReadallFull(io.RawIOBase):
    def read(self, n=-1):
        return b"test"

r = ReadallFull()
assert r.readall() == b"test"

# Test that readall() does not read past the end of the file.
class ReadallPastEnd(io.RawIOBase):
    def read(self, n=-1):
        return b
