import io
# Test io.RawIOBase with a simple implementation of readinto()
# based on read().

class MyIO(io.RawIOBase):
    def __init__(self, data):
        self.data = data
        self.pos = 0
    def read(self, size=-1):
        if 0 <= size <= len(self.data)-self.pos:
            newpos = self.pos + size
        else:
            newpos = len(self.data)
        r = self.data[self.pos:newpos]
        self.pos = newpos
        return r
    def readinto(self, b):
        if not isinstance(b, bytearray) and not isinstance(b, array.array):
            raise TypeError("a bytearray or array.array is required")
        r = self.read(len(b))
        n = len(r)
        try:
            b[:n] = r
        except TypeError as err:
            import array
            if not isinstance(b, array.array) \
               or b.typecode != 'b':

