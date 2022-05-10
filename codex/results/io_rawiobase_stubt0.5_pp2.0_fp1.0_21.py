import io
class File(io.RawIOBase):
    def read(self, n=-1):
        return b''
    def readinto(self, b):
        return 0
    def write(self, b):
        return len(b)
    def fileno(self):
        return -1
    def seekable(self):
        return True
    def seek(self, offset, whence=io.SEEK_SET):
        return 0
    def tell(self):
        return 0
    def truncate(self, size=None):
        return 0
    def flush(self):
        return
    def close(self):
        return


if hasattr(os, 'dup'):
    class FileIO(io.FileIO):
        def __init__(self, fd, mode='r'):
            io.RawIOBase.__init__(self)
            self._fd = fd
            self._mode = mode
            self._offset = 0
            self._reading = False
            self._writing = False
            self._thread_id = thread.get_ident()
            self._blksize = io.DE
