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

def _get_file(file):
    if isinstance(file, (str, bytes)):
        return open(file, 'rb')
    elif hasattr(file, 'read'):
        return file
    elif hasattr(file, 'file'):
        return _get_file(file.file)
    else:
        raise TypeError('file must be a filename, file, or file-like object')

def get_file_size(file):
    file = _get_file(file)
