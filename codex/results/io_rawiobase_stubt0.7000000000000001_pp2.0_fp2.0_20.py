import io
class File(io.RawIOBase):
    def __init__(self, filename, mode="r", *args, **kwargs):
        self._filename = filename
        self._mode = mode
        self._args = args
        self._kwargs = kwargs
        self._file = None
        self.close = self._close
    def __enter__(self):
        return self
    def __exit__(self, *args, **kwargs):
        self.close()
    def _close(self):
        if self._file is not None:
            self._file.close()
            self._file = None
    def readable(self):
        return self._mode == "r"
    def writable(self):
        return self._mode == "w"
    def seekable(self):
        return self._mode == "r"
    def closeable(self):
        return True
    def isatty(self):
        return False
    @property
    def name(self):
        return self._filename
    @property
    def mode(self):
        return self._mode
    def close(self):
