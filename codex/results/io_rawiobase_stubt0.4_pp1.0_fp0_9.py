import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def readinto(self, b):
        data = self.file.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array('b', data)
        return n

def open(file, mode="r"):
    if mode not in ("r", "rb"):
        raise ValueError("FileIO can only open files in binary mode")
    return File(file)

def _test():
    import doctest
    doctest.testmod()

if __name__ == "__main__":
    _test()
