import io
# Test io.RawIOBase.readall that it reads all the data in the stream
# and returns an empty bytes when there is no more data in the stream.
class RawInput0(io.RawIOBase):
    def readable(self):
        return True
    def readinto(self, buf):
        buf[:] = b"0123456789abcdefg"
        return len(buf)
    def seek(self, pos, whence=0):
        return 0
    def tell(self):
        return 0
    def truncate(self, pos=None):
        return 0
inp = RawInput0()
print(inp.readall())
print(inp.readall())
print(inp.readall())
# Test io.RawIOBase.readall that it does not read beyond the given
# size.
class RawInput1(io.RawIOBase):
    def readable(self):
        return True
    def readinto(self, buf):
        buf[:] = b"0123456789abcdefg"
        return len(buf)
    def seek(self, pos, whence
