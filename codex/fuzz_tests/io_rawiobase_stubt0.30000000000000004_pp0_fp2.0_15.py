import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0

    def readinto(self, b):
        """Read up to len(b) bytes into b.

        Returns number of bytes read (0 for EOF).
        """
        if self.closed:
            raise ValueError("read from closed file")

        l = len(b) # We're supposed to return at most this much
        chunk = self.file.read(l)
        n = len(chunk)
        b[:n] = chunk
        return n

    def seek(self, offset, whence=io.SEEK_SET):
        """Change stream position.

        Seek to byte offset offset relative to position indicated by whence:

            0  Start of stream (the default).  offset should be zero or positive.
            1  Current position - offset may be negative.
            2  End of stream - offset is usually negative.

        Returns the new absolute position.
        """
        if self.closed:
            raise ValueError("seek in closed file")

        if whence == 0:
           
