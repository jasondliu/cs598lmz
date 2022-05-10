import io
class File(io.RawIOBase):
    def __init__(self, fp):
        self._fp = fp
        self._len = None
        if isinstance(fp, File):
            self._len = fp._len
            fp = fp._fp

    def seek(self, offset, whence=0):
        return self._fp.seek(offset, whence)

    def tell(self):
        return self._fp.tell()

    def write(self, b):
        n = self._fp.write(b)
        if self._len is None:
            self._len = n
        else:
            self._len += n
        return n

    def read(self, bfsize=0):
        if self._len is not None and self._len < 0:
            raise io.UnsupportedOperation('read')
        elif bfsize <= 0:
            s = self._fp.read()
            if self._len is not None and self._len > 0:
                self._len -= len(s)
            return s
        else:
            return self._fp.read(bfsize)
