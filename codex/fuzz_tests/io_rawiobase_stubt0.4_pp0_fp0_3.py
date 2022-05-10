import io
class File(io.RawIOBase):
    def __init__(self,filename):
        self.filename = filename
    def read(self,size=-1):
        with open(self.filename,"rb") as f:
            return f.read(size)
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return False
    def readall(self):
        return self.read()
    def readinto(self,b):
        data = self.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array(b'b', data)
        return n
    def readline(self,limit=-1):
        if limit < 0:
            limit = io.DEFAULT_BUFFER_SIZE
        data = bytearray()
        while limit:
            c = self.read(1)
            if not
