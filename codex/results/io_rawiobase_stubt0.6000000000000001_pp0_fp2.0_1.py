import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file=file
        self.length=len(file)
        self.position=0
    def readable(self):
        return True
    def readinto(self, b):
        if self.closed:
            raise ValueError("I/O operation on closed file")
        l=len(b)
        result=self.file[self.position:self.position+l]
        n=len(result)
        try:
            b[:n]=result
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n]=array.array(b'b', result)
        self.position += n
        return n
__all__ = ["File"]
