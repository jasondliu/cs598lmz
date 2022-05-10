import io
class File(io.RawIOBase):
    """
    A file-like object that represents a file on a remote server.
    """

    def __init__(self, sftp, handle):
        """
        Initialize the file object.
        """
        self._sftp = sftp
        self._handle = handle

    def close(self):
        """
        Close the file.
        """
        if self._handle is not None:
            self._sftp._close(self._handle)
            self._handle = None
        self._sftp = None

    def seekable(self):
        """
        Return True if the file supports random access.
        """
        return True

    def seek(self, offset, whence=0):
        """
        Move to a new file position.
        """
        self._sftp._seek(self._handle, offset, whence)

    def tell(self):
        """
        Return the current file position.
        """
        return self._sftp._tell(self._handle)

    def readinto(self, b):
        """
        Read bytes
