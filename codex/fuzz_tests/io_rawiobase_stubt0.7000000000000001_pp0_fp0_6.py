import io
class File(io.RawIOBase):
    def __init__(self, fd):
        self.fd = fd

    def readable(self):
        return True

    def writable(self):
        return True

    def seekable(self):
        return True

    def readinto(self, b):
        l = self.fd.read(len(b))
        b[:len(l)] = l
        return len(l)

    def write(self, b):
        self.fd.write(b)
        return len(b)

    def seek(self, offset, whence=io.SEEK_SET):
        if whence == io.SEEK_CUR:
            offset += self.fd.tell()
        elif whence == io.SEEK_END:
            offset += self.fd.seek(0, 2)
        self.fd.seek(offset)
        return self.fd.tell()

    def tell(self):
        return self.fd.tell()

    def close(self):
        self.fd.close()


class FileIO(io.BufferedIOBase):
   
