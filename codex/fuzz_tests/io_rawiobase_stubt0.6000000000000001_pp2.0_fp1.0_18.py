import io
class File(io.RawIOBase):
    def __init__(self, file_path, mode='r'):
        self._file_path = file_path
        self._mode = mode
        self._file = None

    def __del__(self):
        self.close()

    def close(self):
        if self._file:
            self._file.close()

    def open(self):
        self._file = open(self._file_path, self._mode)

    def read(self, size=-1):
        if not self._file:
            raise Exception('File is not open')
        return self._file.read(size)

    def readall(self):
        if not self._file:
            raise Exception('File is not open')
        return self._file.read()

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        if not self._file:
            raise Exception('File is not open')
        return self._file.seek(offset, whence)

    def tell
