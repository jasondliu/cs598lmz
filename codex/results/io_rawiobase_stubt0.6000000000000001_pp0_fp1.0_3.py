import io
class File(io.RawIOBase):
    def __init__(self, filename, mode, *args, **kwargs):
        self._file = open(filename, mode, *args, **kwargs)
        self._mode = mode
        self._pos = 0
        self._closed = False
        self._name = filename
        self._newlines = None
        self._universal_newlines = False

    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()

    def __del__(self):
        if not self._closed:
            self._file.close()

    def close(self):
        if self._closed:
            raise ValueError("I/O operation on closed file.")
        self._closed = True
        self._file.close()

    def fileno(self):
        return self._file.fileno()

    def flush(self):
        self._file.flush()

    def isatty(self):
        return self._file.isatty()

    def readable(self):
        return "r" in self
