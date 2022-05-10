import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r', closefd=True):
        self.name = name
        self.mode = mode
        self.closefd = closefd
        self.fd = None
        self.open(name, mode, closefd)
    def __del__(self):
        self.close()
    def open(self, name, mode='r', closefd=True):
        if self.fd is not None:
            raise ValueError('I/O operation on closed file.')
        if 'b' in mode:
            flags = os.O_RDONLY if 'r' in mode else os.O_WRONLY
            if '+' in mode:
                flags |= os.O_RDWR
            if 'x' in mode:
                flags |= os.O_EXCL
            if 'a' in mode:
                flags |= os.O_APPEND
            if 'w' in mode:
                flags |= os.O_TRUNC
            if '+' in mode:
                flags |= os.O_CREAT
