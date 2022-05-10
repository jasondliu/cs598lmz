import io
class File(io.RawIOBase):
    def __init__(self, file):
        self.file = file
        self.offset = 0
    def readinto(self, b):
        n = self.file.readinto(b)
        self.offset += n
        return n
    def seekable(self):
        return True
    def seek(self, offset, whence=0):
        if whence == 1:
            offset += self.offset
        self.file.seek(offset)
        self.offset = offset
        return self.offset
    def tell(self):
        return self.offset
    def readable(self):
        return True
    def writable(self):
        return False

def open(file, mode="r", buffering=-1, encoding=None, errors=None, newline=None, closefd=True):
    if "b" in mode:
        raise ValueError("binary mode not supported")
    return io.TextIOWrapper(File(file), encoding, errors, newline)

def main():
    with open(sys.argv[1], "r") as f:
