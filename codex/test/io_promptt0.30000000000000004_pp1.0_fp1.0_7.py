import io
# Test io.RawIOBase
class RawI(io.RawIOBase):
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def readinto(self, b):
        return len(b)
    def write(self, b):
        return len(b)
    def seek(self, offset, whence=0):
        return 0
    def tell(self):
        return 0
    def close(self):
        pass

r = RawI()
r.readinto(bytearray(10))
r.write(b"12345")
r.seek(0)
r.tell()
r.close()

# Test io.BufferedIOBase
class BufferedI(io.BufferedIOBase):
    def readable(self):
        return True
    def writable(self):
        return True
    def seekable(self):
        return True
    def readinto(self, b):
        return len(b)
    def write(self, b):
        return len(b)
