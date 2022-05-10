import io
class File(io.RawIOBase):
    """A File-like object that handles serialization for types
    that implement the `Serializable` interface.
    """

    def __init__(self, fh, serializer):
        self._fh = fh
        self._s = serializer
        self._remainder = b''

    def write(self, b):
        if isinstance(b, Serializable):
            return self.write(self._s.serialize(b))
        else:
            return self._fh.write(b)

    def flush(self):
        return self._fh.flush()

    def readinto(self, b):
        if len(self._remainder) > 0:
            l = len(self._remainder)
            b[:l] = self._remainder
            self._remainder = b''
            return l
        else:
            return self._fh.readinto(b)

    def close(self):
        self._fh.close()

    def read(self, size=-1):
        if size == -1:
           
