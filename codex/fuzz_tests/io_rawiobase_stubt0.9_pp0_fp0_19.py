import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        super().__init__()

    def read(self,n=-1):
        return self.file.read(n)

    def readinto(self,b):
        data = self.file.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array("B", data)
        return n


    def write(self,b):
        return self.file.write(b)
        
    def seekable(self):
        return True
        
    def seek(self, pos, whence=io.SEEK_SET):
        if whence == io.SEEK_SET:
            self.file.seek(pos)

        elif whence == io.SEEK_CUR:
            self.file.seek(self.file.tell() + pos)

        elif whence ==
