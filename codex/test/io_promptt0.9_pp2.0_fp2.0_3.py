import io
# Test io.RawIOBase
class IO(io.RawIOBase):
    def readinto(self, b):
        """Read up to len(b) bytes into bytearray b and return
        the number of bytes read.
        """
        b[:] = b'hello world'
        return len(b)
    
    
# Testing subclasses of io.RawIOBase
class Test(IO):
    pass

if __name__ == '__main__':
    io = Test()
    print(io.readinto(bytearray(10)))
    print(io.readinto(bytearray(10)))
