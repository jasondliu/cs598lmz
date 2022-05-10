import io
class File(io.RawIOBase):
    """An io.RawIOBase implementation to wrap a file-like object."""
    def __init__(self, file_like):
        """Initializes the instance with the given file-like object."""
        self._file_like = file_like
        # Ensure that the file-like has a 'write' method.
        if not hasattr(self._file_like, 'write'):
            raise TypeError('{!r} does not have a write method.'.format(
                file_like))

    def read(self, size=-1):
        """Reads and returns up to size bytes.

        Args:
            size (optional): The number of bytes to read.  If omitted, all
                bytes are read.

        Returns:
            bytes: The bytes read.

        Raises:
            IOError: The read failed.
        """
        return self._file_like.read(size)

    def readable(self):
        """Returns True if the instance is readable."""
        return True

    def write(self, b):
        """Writes the given bytes to the file-
