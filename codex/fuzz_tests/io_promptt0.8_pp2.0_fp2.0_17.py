import io
# Test io.RawIOBase with duplicates of file descriptors.

class FDIO(io.RawIOBase):
    def __init__(self, fd):
        self.fd = fd
        self.pos = 0
    def readinto(self, buf):
        n = os.read(self.fd, buf)
        self.pos += len(n)
        return len(n)
    def seek(self, pos, whence=0):
        if whence == 1:
            pos += self.pos
        elif whence == 2:
            pos += os.fstat(self.fd).st_size
        self.pos = pos
        return pos

def test_duplicate():
    fd1 = os.open(__file__, os.O_RDONLY)
    fd2 = os.dup(fd1)
    try:
        # Exercise code path for reading ahead (at EOF).
        i1 = io.BufferedReader(FDIO(fd1), 1000000)
        i2 = io.BufferedReader(FDIO(fd2), 1000000)
       
