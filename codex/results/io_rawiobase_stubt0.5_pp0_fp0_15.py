import io
class File(io.RawIOBase):
    def __init__(self):
        self.offset = 0
    def readinto(self, b):
        n = len(b)
        if self.offset + n > len(data):
            n = len(data) - self.offset
            b = memoryview(b)[:n]
        b[:] = data[self.offset:self.offset+n]
        self.offset += n
        return n

# The following example shows how to implement a read-only file object backed
# by a byte array.

# The readinto() method is called by the file object's read() method. The
# readinto() method is expected to copy data into the given buffer and return
# the number of bytes copied.

# The readinto() method is also used by the io.BufferedReader class to implement
# its read() method.

# The readinto() method is not called when the file object is used as a context
# manager (e.g. using the with statement).
