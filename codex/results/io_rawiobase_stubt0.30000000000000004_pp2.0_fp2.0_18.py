import io
class File(io.RawIOBase):
    def __init__(self, fp):
        self._fp = fp
        self._offset = 0
    def readinto(self, b):
        n = self._fp.readinto(b)
        self._offset += n
        return n
    def seek(self, offset, whence=0):
        if whence == 0:
            self._offset = offset
        elif whence == 1:
            self._offset += offset
        elif whence == 2:
            self._offset = len(self._fp) + offset
        else:
            raise ValueError("Invalid value for `whence`")
        return self._offset
    def tell(self):
        return self._offset
    def readable(self):
        return True
    def writable(self):
        return False
    def seekable(self):
        return True
    def fileno(self):
        return self._fp.fileno()
    def close(self):
        return self._fp.close()
    def flush(self):
        return self._fp.flush()
    def isatty(self):
