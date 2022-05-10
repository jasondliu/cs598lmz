import io
class File(io.RawIOBase):
    """
    A file pointer that can be used in place of a real file.
    """

    def __init__(self):
        self._buffer = b''

    def write(self, data):
        """
        Write data to the file.
        """
        self._buffer += data

    def read(self, size=-1):
        """
        Read data from the file.
        """
        if size == -1:
            size = len(self._buffer)
        else:
            size = min(size, len(self._buffer))
        data = self._buffer[:size]
        self._buffer = self._buffer[size:]
        return data

    def close(self):
        """
        Close the file.
        """
        pass

class FileSaver(io.RawIOBase):
    """
    A file pointer that can be used in place of a real file.
    """

    def __init__(self, filename):
        self._filename = filename
        self._buffer = b''

    def write(self, data):
        """
        Write data
