import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r'):
        self._mode = mode
        self._fd = ofi.OpenFile(path, mode)
        self._offset = 0
        self._size = self.tell()
    def __del__(self):
        self._fd.Close()
    def write(self, buf):
        self._fd.WriteAt(buf, self._offset)
        self._offset += len(buf)
        n = self._fd.EndWriteAt()
        if n > self._size:
            self._size = n
    def tell(self):
        return self._fd.Size()
    def seek(self, offset, whence=0):
        if whence == 0:
            self._offset = offset
        elif whence == 1:
            self._offset += offset
        else:
            self._offset = self._size + offset
    def readinto(self, buf):
        n = len(buf)
        assert n >= 0
        data = self._fd.ReadAt(n, self._offset)
        buf[:len(
