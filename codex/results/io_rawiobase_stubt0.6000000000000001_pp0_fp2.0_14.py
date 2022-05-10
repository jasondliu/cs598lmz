import io
class File(io.RawIOBase):
    """
    A file-like object.
    """

    def __init__(self, file_path):
        self._file_path = file_path
        self._file_handle = None
        self._buffer = None
        self._buffer_offset = 0
        self._buffer_size = 0

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

    @property
    def closed(self):
        """
        Whether the file is closed.
        :rtype: bool
        """
        return self._file_handle is None

    def close(self):
        """
        Close the file.
        """
        if self._file_handle is not None:
            self._file_handle.close()
        self._file_handle = None
        self._buffer = None
        self._buffer_offset = 0
        self._buffer_size = 0

    def open(self, mode="rb"):
        """
        Open the file.
        :param str
