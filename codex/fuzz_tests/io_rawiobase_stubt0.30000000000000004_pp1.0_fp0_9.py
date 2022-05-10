import io
class File(io.RawIOBase):
    """
    A file-like object that reads and writes to a file on disk.
    """
    def __init__(self, path, mode='r'):
        self.path = path
        self.mode = mode
        self._file = None
        self._buffer = None
        self._buffer_size = 1024 * 1024
        self._buffer_pos = 0
        self._buffer_end = 0
        self._closed = False

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    def close(self):
        if self._closed:
            return
        if self._buffer is not None:
            self._flush_buffer()
        if self._file is not None:
            self._file.close()
        self._closed = True

    def readable(self):
        return 'r' in self.mode

    def writable(self):
        return 'w' in self.mode

    def seekable(self):
        return True

    def seek(
