import io
# Test io.RawIOBase
class Stream(io.RawIOBase):
    def readinto(self, buf):
        raise NotImplementedError

stream = Stream()
stream.readinto(bytearray(1))

# Test io.BufferedIOBase
class StringIO(io.BufferedIOBase):
    def __init__(self, bytes):
        self.bytes = bytes

    def readinto(self, buf):
        if len(self.bytes) > len(buf):
            buf[:] = self.bytes[:len(buf)]
            self.bytes = self.bytes[len(buf):]
            return len(buf)
        else:
            buf[:len(self.bytes)] = self.bytes
            l = len(self.bytes)
            self.bytes = b''
            return l

s = StringIO(b'abc')
buf = bytearray(2)
s.readinto(buf)
print(buf)
s.readinto(buf)
print(buf)
s.readinto(buf)
print(buf)

s = StringIO
