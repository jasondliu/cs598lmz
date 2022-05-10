import io
class File(io.RawIOBase):
    """A file-like object for communicating with a child process."""
    def __init__(self, name, mode, closefd, opener=None):
        self._name = name
        self._mode = mode
        self._closefd = closefd
        if opener is not None:
            self._opener = opener
        else:
            self._opener = builtins.open

    def __repr__(self):
        s = "<_io.File name=%r mode=%r closefd=%r>" % (
            self._name, self._mode, self._closefd)
        return s

    def readable(self):
        return "r" in self._mode

    def writable(self):
        return "w" in self._mode

    def seekable(self):
        return False

    def fileno(self):
        return self._name

    def close(self):
        if self._closefd:
            # File was opened by Popen; delegate close to Popen.
            pass
        else:
            # File was opened by us; delegate close to us
