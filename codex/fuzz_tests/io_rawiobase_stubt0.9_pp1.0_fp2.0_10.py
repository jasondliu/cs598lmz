import io
class File(io.RawIOBase):
"""Faked file object attached to a real file descriptor.
This makes it possible to use a real file descriptor in a with
statement, and have the file closed automatically.
"""
def __init__(self, fd):
    self.__fd = fd
    self.__closed = False
    _os.set_blocking(fd, False)

def __repr__(self):
    return '<_fileio.%s fd=%r>' % (self.__class__.__qualname__, self.__fd)

def readable(self):
    return True

def writable(self):
    return True

def seekable(self):
    return False

def fileno(self):
    return self.__fd

def close(self):
    if not self.closed:
        self.closed = True
        self.flush()
        if hasattr(self, 'detach'):
            self.detach()

@property
def closed(self):
    return self.__closed

def detach(self):
    fd = self.__
