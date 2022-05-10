import io
class File(io.RawIOBase):
    def __init__(self, file, mode="r"):
        self._file = file
        self._mode = mode
        self._reading = "r" in mode
        self._writing = "w" in mode
        self._closed = False
        self._pos = 0

    def readinto(self, b):
        if not self._reading:
            raise io.UnsupportedOperation("not readable")
        if self._closed:
            raise ValueError("I/O operation on closed file")
        l = self._file.readinto(b)
        self._pos += l
        return l

    def write(self, b):
        if not self._writing:
            raise io.UnsupportedOperation("not writeable")
        if self._closed:
            raise ValueError("I/O operation on closed file")
        l = self._file.write(b)
        self._pos += l
        return l

    def seek(self, pos, whence=io.SEEK_SET):
        if self._closed:
            raise ValueError("I/O operation on closed file")
       
