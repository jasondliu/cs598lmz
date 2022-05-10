import io
class File(io.RawIOBase):
    """A File-like object.

    :param file_name: the name of the file

    This class is initialized with a file name, and implements the basic methods
    to read and write.
    """

    _file = None

    def __init__(self, file_name, mode='r'):
        self._file_name = file_name
        self._mode = mode
        self._file = open(file_name, mode)

    def read(self, size=-1):
        """Reads `size` bytes from the file (or less, if there aren't that many
        left) and returns them.

        If `size` is negative or omitted, read until EOF and return all read
        bytes.

        If the end of the file has been reached, this will return an empty string
        (``''``).
        """
        return self._file.read(size)

    def readinto(self, b):
        """Reads up to len(b) bytes into b, and returns the number of bytes read
        (0 for EOF)."""
        return self._file.read
