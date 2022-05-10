import io
class File(io.RawIOBase):
    def __init__(self, fd):
        self._fd = fd
    def readinto(self, b):
        n = os.read(self._fd, b)
        return n

f = open('/test.txt', 'rb')
afile = File(f.fileno())
print(afile.readinto(b'hello'))
