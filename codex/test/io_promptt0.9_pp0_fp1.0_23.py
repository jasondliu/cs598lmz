import io
# Test io.RawIOBase error handling techniques
class BadIO(io.RawIOBase):
    def readable(self):
        return True
    def readinto(self, buf):
        raise self.MyException("fake exception")
    class MyException(Exception):
        pass

# Test a variety of read() lengths
class GoodIO(io.RawIOBase):
    def __init__(self):
        self.data = b"abcdefghijklmnopqrstuvwxyz"
    def readable(self):
        return True
    def readinto(self, buf):
        n = len(buf)
        if len(buf) > len(self.data):
            n = len(self.data)
        print ("readinto(len={0}) = {1}".format(n, self.data[0:n]))
        buf[0:n] = self.data[0:n]
        self.data = self.data[n:]
        if n > 0:
            return n
        else:
            return None
