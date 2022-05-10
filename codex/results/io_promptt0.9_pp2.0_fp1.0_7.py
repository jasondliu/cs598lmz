import io
# Test io.RawIOBase
class FileIO(io.RawIOBase):
    def __init__(self, path, mode):
        self.fd = os.open(path, mode)
        if 'b' not in mode:
            raise ValueError("binary mode required")
        self._modes = mode

    def close(self):
        # os.close(self.fd)
        super().close()

    def fileno(self):
        return self.fd

    def _write(self, b):
        pass

    def _read(self, max_count=1):
        return os.read(self.fd, max_count)

    @property
    def read(self):
        if 'r' not in self._modes:
            raise AttributeError("read not supported")
        return self._read

    @property
    def seekable(self):
        return False

    @property
    def write(self):
        if 'w' not in self._modes:
            raise AttributeError("write not supported")
        return self._write

    @property
    def readable(self):
