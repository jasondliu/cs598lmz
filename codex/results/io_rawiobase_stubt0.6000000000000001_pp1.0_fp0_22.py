import io
class File(io.RawIOBase):
    '''A class for reading and writing files.
    '''
    def __new__(cls, *args, **kwargs):
        if cls is File:
            return object.__new__(full_file)
        else:
            return object.__new__(cls)


class full_file(File):
    '''A file-like object for reading and writing files.
    '''
    def __init__(self, filepath, mode='rb', buffering=-1, encoding=None,
                 errors=None, newline=None, closefd=True, opener=None):
        self.filepath = filepath
        self.mode = mode
        self.encoding = encoding
        self.errors = errors
        self.newline = newline
        self.closefd = closefd
        if opener is not None:
            self.fd = opener(self.filepath, self.mode, self.closefd)
        else:
            self.fd = os.open(self.filepath, self.mode, self.closefd)
        self.readable =
