import io
class File(io.RawIOBase):
    def __init__(self, fd):
        self.fd = fd
    def readable(self):
        return True
    def readinto(self, buf):
        return os.readv(self.fd, [buf])

class AStream(io.RawIOBase):
    def __init__(self, fd):
        self.fd = fd
    def readable(self):
        return True
    def readinto(self, buf):
        return os.readv(self.fd, [buf])

class AFile(AFileIO):
    def __init__(self, fd):
        self.fd = fd
    def readable(self):
        return True
    def readinto(self, buf):
        return os.readv(self.fd, [buf])

def main():
    f = open("/dev/stdin")
    print(type(f))
    print(type(File(f.fileno())))
    print(type(AFile(f.fileno())))
    print(type(AStream(f.fil
