import io
class File(io.RawIOBase):
    """
    File-like class that reads from a string.
    """

    def __init__(self, buffer=None):
        self.buffer = buffer
        self.offset = 0

    def readable(self):
        return True

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        if whence == 0:
            self.offset = offset
        elif whence == 1:
            self.offset += offset
        elif whence == 2:
            self.offset = len(self.buffer) + offset
        return self.offset

    def tell(self):
        return self.offset

    def readinto(self, b):
        o = self.offset
        l = len(b) # the length of the target buffer
        s = self.buffer # the source string
        sl = len(s) # the length of the source string
        self.offset = min(o + l, sl)
        if o >= sl:
            return 0
        b[:sl-o] = s[o:self.offset]
        return self
