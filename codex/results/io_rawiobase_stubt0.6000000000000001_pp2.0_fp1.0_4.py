import io
class File(io.RawIOBase):
    """
    I can't think of a great way to handle this.  I'm going to assume that if
    the file is created with a ``mode`` of ``w`` or ``a``, then it's a
    writable file, otherwise it's read-only.  This will be wrong sometimes,
    but it's probably better than the alternative, which is to assume that the
    file is writable and then raise an exception when the user tries to write
    to a read-only stream.
    """
    def __init__(self, stream):
        self._stream = stream

    def close(self):
        self._stream.close()

    def readable(self):
        return not self._stream.closed

    def writable(self):
        return not self._stream.closed

    def seekable(self):
        return False

    def readinto(self, b):
        return self._stream.readinto(b)

    def readall(self):
        return self._stream.readall()

    def read1(self, n):
        return self._stream.read(n)

   
