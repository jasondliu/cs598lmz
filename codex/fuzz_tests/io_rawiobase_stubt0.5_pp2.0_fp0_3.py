import io
class File(io.RawIOBase):
    def __init__(self, filepath, mode='r', closefd=True, opener=None):
        self.filepath = filepath
        self.mode = mode
        self.closefd = closefd
        self.opener = opener
        self.fd = None
        self.open(filepath, mode, closefd, opener)
    def close(self):
        if self.fd is not None:
            os.close(self.fd)
    def open(self, filepath, mode='r', closefd=True, opener=None):
        if not self.fd is None:
            raise ValueError('I/O operation on closed file')
        if not hasattr(os, 'O_BINARY'):
            os.O_BINARY = 0
        flags = os.O_BINARY
        if 'r' in mode:
            if '+' in mode:
                flags |= os.O_RDWR
            else:
                flags |= os.O_RDONLY
        elif 'w' in mode:
            flags |= os.
