import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r', buffering=-1, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        ...
    def __enter__(self):
        ...
    def __exit__(self, exc_type, exc_val, exc_tb):
        ...
    def __iter__(self):
        ...
    def close(self):
        ...
    def fileno(self):
        ...
    def flush(self):
        ...
    def isatty(self):
        ...
    def readable(self):
        ...
    def readline(self, size=-1):
        ...
    def readlines(self, hint=-1):
        ...
    def seek(self, offset, whence=0):
        ...
    def seekable(self):
        ...
    def tell(self):
        ...
    def truncate(self, size=None):
        ...
    def writable(self):
        ...
    def writelines(self, lines):
        ...
    def
