import io
# Test io.RawIOBase.readall()

class MyRawIO(io.RawIOBase):
    def __init__(self, data):
        self._data = data
    def readinto(self, buf):
        if len(buf) >= len(self._data):
            buf[:] = self._data
            return len(self._data)
        else:
            buf[:len(self._data)] = self._data[:len(buf)]
            return len(buf)

try:
    io.RawIOBase.readall
except AttributeError:
    pass
else:
    print(MyRawIO(b'abc').readall())
    print(MyRawIO(b'abc').readall(2))
    print(MyRawIO(b'abc').readall(4))
