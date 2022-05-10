import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self._fp = None
    def open(self, mode=None):
        self._fp = open(self.name, mode)
    def read(self, size=-1):
        return self._fp.read(size)
    def readline(self, size=-1):
        return self._fp.readline(size)
    def write(self, data):
        self._fp.write(data)
    def seek(self, offset, whence=0):
        self._fp.seek(offset, whence)
    def tell(self):
        return self._fp.tell()
    def close(self):
        self._fp.close()
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, type, value, traceback):
        self.close()

with File('test.txt') as f:
    f.write('hello, world')

print(f.name)

# io.IOBase
# io.RawIOBase
