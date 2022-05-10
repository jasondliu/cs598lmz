import io
class File(io.RawIOBase):
    def __init__(self, filename, mode, buffering=0, encoding=None, errors=None, newline=None, closefd=True, opener=None):
        if 'r' in mode:
            mode = mode.replace('r', 'w')

        if mode:
            self._mode = mode
        else:
            self._mode = 'w'
        self._name = filename
        self._writable = (self._mode[0]=='w')

        if self._writable:
            self._buffer = io.BytesIO()
        else:
            self._buffer = None

    def readable(self):
        return False

    def writable(self):
        return True

    def seekable(self):
        return False

    def flush(self):
        pass

    def isatty(self):
        return False

    def read(self, size=-1):
        raise io.UnsupportedOperation

    def write(self, b):
        self._buffer.write(b)

    def tell(self):
        return self._buffer.tell()

   
