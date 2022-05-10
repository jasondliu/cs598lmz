import io
class File(io.RawIOBase):
    """A file-like object that logs all operations."""
    def __init__(self, name, mode, file):
        self.name = name
        self.mode = mode
        self.file = file
        # These are just for demonstration.
        # They probably should not be written to a log.
        self.softspace = 0
        self.closed = False
        self.newlines = None
        self.encoding = None
        self.errors = None
        self.log('open')
    def write(self, s):
        self.log('write', repr(s))
        self.file.write(s)
    def read(self, n=-1):
        self.log('read', n)
        return self.file.read(n)
    def flush(self):
        self.log('flush')
        self.file.flush()
    def close(self):
        self.log('close')
        self.file.close()
        self.closed = True
    def __getattr__(self, name):
        return getattr(self.file,
