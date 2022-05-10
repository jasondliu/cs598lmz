import io
class File(io.RawIOBase):
    """
    File-like object.
    """
    def __init__(self, file_obj):
        self._file_obj = file_obj
        self._file_obj.seek(0, os.SEEK_END)
        self._size = self._file_obj.tell()
        self._file_obj.seek(0)

    def read(self, size=-1):
        return self._file_obj.read(size)

    def seek(self, offset, whence):
        return self._file_obj.seek(offset, whence)

    def tell(self):
        return self._file_obj.tell()

    def readable(self):
        return True

    def writable(self):
        return False

    def seekable(self):
        return True

    def fileno(self):
        return self._file_obj.fileno()

    @property
    def size(self):
        return self._size


class ProgressPercentage(object):
    """
    Helper class to track S3 uploads.
    """
    def __init__(
