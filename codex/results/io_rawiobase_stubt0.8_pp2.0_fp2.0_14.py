import io
class File(io.RawIOBase):
    def __init__(self):
        self.open(file_name, mode)
        self.closed = True
        self._writing = False
        self._reading = False
        self._read_fd = None
        self._write_fd = None
        self._tell = None
        self._read_lock = None
        self._write_lock = None

    def fileno(self):
        if self._read_fd is not None:
            return self._read_fd
        else:
            return self._write_fd

    def open(self, file_name, mode, closefd=True):
        raise NotImplementedError

    def flush(self):
        if self._writing:
            os.fdatasync(self._write_fd)
        if self._reading:
            os.fdatasync(self._read_fd)

    def close(self):
        raise NotImplementedError

    def __repr__(self):
        return Object.__repr__(self) + f': {self.name}'

class Text_SourceFile(File
