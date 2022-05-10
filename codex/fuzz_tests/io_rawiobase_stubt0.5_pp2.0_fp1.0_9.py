import io
class File(io.RawIOBase):
    """
    Raw file object.
    """
    def __init__(self, name, mode='r', closefd=True):
        if mode not in ('r', 'w', 'rw', 'wr'):
            raise ValueError("invalid mode: %r" % mode)
        io.RawIOBase.__init__(self)
        self.mode = mode
        self.closefd = closefd
        self.name = name
        if 'r' in mode:
            self.fd = os.open(name, os.O_RDONLY)
        elif 'w' in mode:
            self.fd = os.open(name, os.O_WRONLY | os.O_CREAT)
        elif '+' in mode:
            self.fd = os.open(name, os.O_RDWR | os.O_CREAT)
        else:
            raise ValueError("invalid mode: %r" % mode)

    def close(self):
        if self.closefd:
            os.close(self.fd)
            self.fd
