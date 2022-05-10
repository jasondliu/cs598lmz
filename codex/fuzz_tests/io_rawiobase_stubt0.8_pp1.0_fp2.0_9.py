import io
class File(io.RawIOBase):
    """Proxy for (file) objects; does not own underlying file.
    """
    def __init__(self, file):
        self.file = file
        self._read = file.read
        self._readinto = file.readinto
        self._write = file.write
        self._seek = file.seek
        try:
            self.name = file.name
        except AttributeError:
            pass
    def seekable(self):
        return True
    def readable(self):
        return True
    def writable(self):
        return True
    def fileno(self):
        return self.file.fileno()
    def readable(self):
        return True
    def write(self, b):
        self._write(b)
    def seek(self, pos, whence=0):
        self._seek(pos, whence)
    def flush(self):
        self.file.flush()

try:
    import ctypes
    ctypes.c_ssize_t
    HAVE_CTYPES = True
except (ImportError, AttributeError):
