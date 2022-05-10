import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def readinto(self, b):
        data = self.f.read(len(b))
        n = len(data)
        try:
            b[:n] = data
        except TypeError as err:
            import array
            if not isinstance(b, array.array):
                raise err
            b[:n] = array.array(b'b', data)
        return n

def open(file, mode="r"):
    """Open a file, returning an object of the file type described above.

    The mode can be 'r', 'w' or 'a' for reading (default), writing or
    appending.  The file will be created if it doesn't exist when opened
    for writing or appending; it will be truncated when opened for
    writing.  Add a '+' to the mode to allow simultaneous reading and
    writing.  Add a 'b' to the mode to make the
