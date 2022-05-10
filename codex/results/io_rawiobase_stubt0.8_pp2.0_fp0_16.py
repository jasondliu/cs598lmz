import io
class File(io.RawIOBase):
    """
    File(filename, mode='r', *, buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None)
    Open file and return a corresponding file object.  Raises OSError upon failure.
    """
    def __init__(self,file,mode='r',buffering=-1,encoding=None,errors=None,newline=None, closefd=True,opener=None):
        self.file = file
        self.mode = mode
        self.buffering = buffering
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        self.opener = opener

    def __enter__(self):
        self.descriptor = os.open(self.file, self.mode, self.buffering)
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        self.descriptor = None
    def flush(self):
        self.descriptor.
