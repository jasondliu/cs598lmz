import io
# Test io.RawIOBase
class MyRawIOWrapper(io.RawIOBase):
    def writable(self):
        return False

    def readable(self):
        return True

    def fileno(self):
        return -1

    def seekable(self):
        return False

    def read(self, size=-1):
        return u'Test'.encode('utf-16')

    def readinto(self, buffer):
        return len(self.read(100))

    def readall(self):
        return self.read()

    def write(self, data):
        return None

read_only = MyRawIOWrapper()

f = read_only.readline
f()
f = read_only.readlines
f()
f = read_only.seek
try:
    f(0)
except OSError:
    print('OSError')

# Test io.BufferedIOBase
class MockRawIO(io.RawIOBase):
    def __init__(self, value):
        self._value = value
        self._pos = 0
       
