import io
class File(io.RawIOBase):
    def __init__(self, fd, mode):
        self.fd = fd
        self.mode = mode
        self.readable = 'r' in mode
        self.writable = 'w' in mode
        self.seekable = True
        self.tell = 0

    def readinto(self, b):
        n = self.fd.readinto(b)
        self.tell += n
        return n

    def write(self, b):
        n = self.fd.write(b)
        self.tell += n
        return n

    def seek(self, offset, whence=0):
        if whence == 0:
            self.tell = offset
        elif whence == 1:
            self.tell += offset
        elif whence == 2:
            self.tell = len(self.fd) + offset
        else:
            raise ValueError("Invalid value for 'whence'")
        self.fd.seek(self.tell)

    def tell(self):
        return self.tell

def open(fd, mode='r'):
    return File
