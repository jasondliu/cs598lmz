import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
    def read(self, n=-1):
        return self.file.read(n)
    def readall(self):
        return self.file.read()
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

def open(file, mode="rb", buffering=-1, encoding=None,
         errors=None, newline=None, closefd=True, opener=None):
    if isinstance(file, (str, bytes)):
        return io.open(file, mode, buffering, encoding, errors, newline, opener)
    if buffering == 0:
        raise ValueError("unbuffered streams must be binary")
    if buffering <
