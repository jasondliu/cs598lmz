import io
class File(io.RawIOBase):
    def __init__(self, path, mode):
        self.fd = open(path, mode)
    def readinto(self, b):
        return self.fd.readinto(b)
    def write(self, b):
        return self.fd.write(b)
    def __getattr__(self, name):
        return getattr(self.fd, name)

class FileArray(np.ndarray):
    def __new__(cls, path, dtype=np.float32, shape=None, offset=0, order='C'):
        if shape is None:
            shape = (os.stat(path).st_size - offset) // np.dtype(dtype).itemsize
        if offset != 0:
            self = np.ndarray.__new__(cls, shape, dtype, buffer=File(path, 'rb'), offset=offset, order=order)
        else:
            self = np.ndarray.__new__(cls, shape, dtype, buffer=File(path, 'rb'), order=order)
        self
