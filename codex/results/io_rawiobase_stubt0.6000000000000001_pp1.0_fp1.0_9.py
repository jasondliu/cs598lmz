import io
class File(io.RawIOBase):
    def __init__(self, fd):
        self.fd = fd
    def read(self, n=-1):
        return os.read(self.fd, n)
    def write(self, b):
        return os.write(self.fd, b)
    def close(self):
        return os.close(self.fd)
    def fileno(self):
        return self.fd
    def isatty(self):
        return False
    def __repr__(self):
        return '<file fd=%d>' % self.fd
def fdopen(fd, mode='r', buffering=-1):
    if buffering == 0:
        buffering = -1
    if buffering < 0:
        buffering = io.DEFAULT_BUFFER_SIZE
    if 'b' in mode:
        mode = mode.replace('b', '')
        binary = True
    else:
        binary = False
    if 't' in mode:
        mode = mode.replace('t', '')
        if binary:
            raise
