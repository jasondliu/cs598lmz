import io
# Test io.RawIOBase
# No need to implement readinto()
class RawIOTest(io.RawIOBase):
    def read(self, size=-1):
        return b'a' * size
    def write(self, b):
        return len(b)

f = RawIOTest()
print(f.read(10))
print(f.write(b'abcdef'))
print(f.read())
print(f.write(b'ghijkl'))
f.close()

# Test io.BufferedIOBase
# No need to implement readinto() and write()
class BufferedIOTest(io.BufferedIOBase):
    def __init__(self, raw):
        self._raw = raw
    def read(self, size=-1):
        return self._raw.read(size)
    def write(self, b):
        return self._raw.write(b)
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def close(self):

