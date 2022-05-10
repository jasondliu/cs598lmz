import io
class File(io.RawIOBase):
    def __init__(self, fd):
        self._fd = fd
    def readable(self):
        return True
    def seekable(self):
        return True
    def writable(self):
        return True

    def fileno(self):
        return self._fd

    def readinto(self, b):
        buf = _read(self._fd, len(b))
        if len(buf) != len(b):
            raise BlockingIOError(
                "Attempted to read {0} bytes but only got {1}.".format(
                    len(b), len(buf)))
        return buf

    def write(self, b):
        _write(self._fd, bytes(b))
        return len(b)

    def seek(self, pos, whence=0):
        if whence == 0:
            return _seek(self._fd, pos)
        elif whence == 1:
            res = _tell(self._fd)
            _seek(pos, 1)
            return res
        elif whence == 2:
            return _seek(
