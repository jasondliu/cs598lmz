import io
class File(io.RawIOBase):
    def __init__(self, filename):
        super(File, self).__init__()
        self._fp = io.open(filename, 'rb')

    def close(self):
        self._fp.close()

    def __del__(self):
        self._fp.close()

    def readinto(self, b):
        return self._fp.readinto(b)

f = File("/etc/passwd")
print(type(f))
print(f)
print(f.read(2))
print(f.read(2))
print(f.read(2))
print(f.read(2))
