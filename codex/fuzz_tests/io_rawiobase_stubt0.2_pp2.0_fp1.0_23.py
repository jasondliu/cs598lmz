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
            b[:n] = array.array(b'b', data)
        return n

def open(file, mode="rb", buffering=-1, encoding=None, errors=None, newline=None, closefd=True):
    if newline is not None:
        raise ValueError("newline is not supported in pytype")
    if not closefd:
        raise ValueError("closefd is not supported in pytype")
    if buffering == 0 or buffering is None:
        buffering = -1
    if buffering < 0:
        buffering = io.DEFAULT_BUFFER
