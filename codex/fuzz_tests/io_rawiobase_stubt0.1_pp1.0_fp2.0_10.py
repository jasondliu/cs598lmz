import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0

    def readinto(self, b):
        """Read up to len(b) bytes into bytearray b and return the number of bytes read.
        If the end of the file is reached, return 0.
        """
        if self.closed:
            raise ValueError("I/O operation on closed file.")
        l = len(b) # We're supposed to return at most this much
        chunk = self.file.read(l)
        b[:len(chunk)] = chunk
        self.offset += len(chunk)
        return len(chunk)

    def seekable(self):
        return True

    def seek(self, offset, whence=io.SEEK_SET):
        if self.closed:
            raise ValueError("I/O operation on closed file.")
        if whence == io.SEEK_CUR:
            offset += self.offset
        elif whence == io.SEEK_END:
            offset += self.file.size
        self.
