import io
class File(io.RawIOBase):
    """
    This class is intended to be a minimal implentation of the
    io.RawIOBase class. For example, it omits the writable() and
    writelines() methods
    """
    def __init__(self, filename):
        self.filename = filename
        self.pos = 0

    def readable(self):
        """
        bool: Should return True if the stream supports random access,
        False otherwise. If getbuffer() or readinto() is supported,
        this method should also return True.
        """
        return True

    def seekable(self):
        """
        bool: Should return True if the stream supports random access,
        False otherwise. If getbuffer() or readinto() is supported,
        this method should also return True.
        """
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        """
        Change the stream position to the given byte offset.
        Offset is interpreted relative to the position indicated
        by whence. Values for whence are:

            - 0: start of stream (the default); offset should be zero or
