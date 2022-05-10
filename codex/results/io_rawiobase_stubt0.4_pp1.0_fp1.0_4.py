import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0

    def readinto(self, b):
        """Read up to len(b) bytes into bytearray b and return the number of bytes read.
        If the end of the file is reached, return 0 instead of raising EOFError.
        """
        if self.closed:
            raise ValueError("readinto on closed file")
        l = self.file.readinto(b)
        self.offset += l
        return l

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        """Change the stream position to the given byte offset.
        The offset is interpreted relative to the position indicated by whence.
        Values for whence are:
        * 0 -- start of stream (the default); offset should be zero or positive
        * 1 -- current stream position; offset may be negative
        * 2 -- end of stream; offset is usually negative
        Return the new absolute position.
        """
        if self.
