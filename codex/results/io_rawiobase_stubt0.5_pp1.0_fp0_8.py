import io
class File(io.RawIOBase):
    """
    A class to wrap the mongodb GridFS file
    """
    def __init__(self, file, mode):
        """
        Initialize the File class
        """
        self.file = file
        self.mode = mode

    def write(self, b):
        """
        Write the bytes to the file
        """
        return self.file.write(b)

    def read(self, size=-1):
        """
        Read the bytes from the file
        """
        return self.file.read(size)

    def readable(self):
        """
        Return whether the file is readable
        """
        return 'r' in self.mode

    def writable(self):
        """
        Return whether the file is writable
        """
        return 'w' in self.mode

    def seekable(self):
        """
        Return whether the file is seekable
        """
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        """
        Seek to the specified offset
        """
        return self
