import io
# Test io.RawIOBase.readall on a stream which supports readall.

class MyStream(io.RawIOBase):
    def __init__(self, data):
        self._data = data
    def readinto(self, b):
        if self._data:
            b[:len(self._data)] = self._data
            self._data = b""
            return len(self._data)
        return 0
    def readall(self):
        data = self._data
        self._data = b""
        return data

stream = MyStream(b"data")
