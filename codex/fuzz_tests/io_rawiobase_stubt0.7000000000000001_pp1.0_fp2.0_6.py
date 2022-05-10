import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
    def read(self, n = -1):
        f = open(self.name, 'rb')
        if n == -1:
            ret = f.read()
        else:
            ret = f.read(n)
        f.close()
        return ret.decode('utf-8')
    def tell(self):
        return 0
    def seek(self, n, whence = io.SEEK_SET):
        pass
    def close(self):
        pass

def open(name, mode='r', buffering = -1, encoding=None,
         errors=None, newline=None, closefd=True, opener=None):
    if 'b' in mode:
        raise NotImplementedError
    if '+' in mode:
        raise NotImplementedError
    if 'x' in mode:
        raise NotImplementedError
    if 'U' in mode:
        raise NotImplementedError
    if 'r' in mode:
        return File(
