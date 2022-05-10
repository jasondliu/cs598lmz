import io
class File(io.RawIOBase):
    def __init__(self, file_path, mode='r'):
        self._file_path = file_path
        self._mode = mode
        self._file_handle = None
        self._offset = 0
        self._opened = False
        self._closed = False

    def open(self):
        if self._opened:
            return
        self._file_handle = open(self._file_path, self._mode)
        self._opened = True

    def close(self):
        if not self._closed:
            self._file_handle.close()
            self._closed = True

    def read(self, size=-1):
        self.open()
        data = self._file_handle.read(size)
        self._offset += len(data)
        return data

    def tell(self):
        return self._offset

    def seek(self, offset, whence=io.SEEK_SET):
        self.open()
        self._file_handle.seek(offset, whence)
        self._offset = self._file_handle.tell()
        return self
