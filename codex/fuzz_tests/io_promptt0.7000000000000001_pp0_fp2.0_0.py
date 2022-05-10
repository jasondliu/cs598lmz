import io
# Test io.RawIOBase class

# io.RawIOBase is not intended to be instantiated directly.
# Instead, a class inheriting from it should override readinto(),
# read() and write().

# http://docs.python.org/2/library/io.html#raw-i-o

class MyRawIO(io.RawIOBase):
    
    def readinto(self, b):
        print("readinto: ", b)
        return len(b)
    
    def read(self, n = -1):
        print("read: ", n)
        return "123"
    
    def write(self, b):
        print("write: ", b)
        return len(b)

raw_io = MyRawIO()

raw_io.read()
raw_io.readinto(bytearray())
raw_io.write("456")
raw_io.readinto(bytearray())
raw_io.readinto(bytearray())
raw_io.write("789")

# Test io.BufferedIOBase class

# io.Buffered
