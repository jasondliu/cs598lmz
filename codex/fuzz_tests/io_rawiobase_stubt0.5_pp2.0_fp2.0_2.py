import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self._fp = io.open(name, 'rb')

    def read(self, size=-1):
        return self._fp.read(size)

    def readinto(self, b):
        return self._fp.readinto(b)

    def close(self):
        self._fp.close()

    def __repr__(self):
        return 'File(%r)' % self.name

f = File('/home/ubuntu/Downloads/test.txt')
print(f.read(5))
f.close()
