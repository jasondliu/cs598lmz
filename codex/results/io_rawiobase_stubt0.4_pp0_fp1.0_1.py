import io
class File(io.RawIOBase):
    def __init__(self, f):
        self.f = f
    def read(self, n=-1):
        return self.f.read(n)
    def write(self, b):
        self.f.write(b)
        return len(b)
    def close(self):
        return self.f.close()

def file_open(filename, mode='r'):
    """Open a file, returning an object of the file type described in section
       10.1.

       If the file cannot be opened, IOError is raised.  When opening a file,
       it's preferable to use open() instead of invoking this constructor
       directly.
    """
    if mode.startswith('r'):
        return File(open(filename, mode))
    elif mode.startswith('w'):
        return File(open(filename, mode))
    raise ValueError('invalid mode: %s' % mode)

def file_input(files=None):
    """Create an object to read data from the list of files given by *files*,
       which
