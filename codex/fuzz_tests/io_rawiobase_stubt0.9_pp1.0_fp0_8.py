import io
class File(io.RawIOBase):
    """A file-like object for reading and writing binary data.

    Created by calling the built-in :func:`open` function.
    """
    default_bufsize = size = 0
    def __init__(self):
        self.file = lib.File_new()

    def __del__(self):
        lib.File_close(self.file)

    def close(self):
        """Close the file.

        A closed file cannot be used for further I/O operations.
        close() may be called more than once without error.
        """
        lib.File_close(self.file)
    
    def readinto(self, b):
        """Read up to len(b) bytes into bytearray b and return
        the number of bytes read. If the end of the file
        has been reached, b will be empty.
        """
        length = len(b)
        n = lib.File_read(self.file, b, length)
        if n >= 0:
            b[n:] = ""
            return n
        else:
            raise O
