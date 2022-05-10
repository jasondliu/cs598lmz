import io
class File(io.RawIOBase):
    def __init__(self, path):
        self._path = path
        self._file = open(self._path, 'rb')
        self._bytes_read = 0

    def read(self, size=None):
        data = self._file.read(size)
        self._bytes_read += len(data)
        return data

    def tell(self):
        return self._bytes_read

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_CUR:
            offset += self._bytes_read
        elif whence == io.SEEK_END:
            offset += self._file.seek(0, io.SEEK_END)
        self._file.seek(offset, io.SEEK_SET)
        self._bytes_read = offset
        return self._bytes_read

    def close(self):
        self._file.close()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.
