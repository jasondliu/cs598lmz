import io
class File(io.RawIOBase):
    def __init__(self, fobj):
        self.fobj = fobj

    def readable(self):
        return True

    def readinto(self, b):
        n = len(b)
        view = memoryview(b).cast("B")
        while n &gt; 0:
            buf = self.fobj.read(n)
            if not buf:
                break
            view[:len(buf)] = buf
            view = view[len(buf):]
            n -= len(buf)
        return len(b) - n

    def seekable(self):
        return True

    def seek(self, offset, whence=0):
        if whence == 0:
            self.fobj.seek(offset)
        elif whence == 1:
            self.fobj.seek(self.fobj.tell() + offset)
        elif whence == 2:
            self.fobj.seek(len(self.fobj) + offset)
        else:
            raise ValueError("Invalid value for whence")

    def tell(self):
        return self
