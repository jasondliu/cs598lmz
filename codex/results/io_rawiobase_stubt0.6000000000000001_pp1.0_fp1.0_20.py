import io
class File(io.RawIOBase):
    def __init__(self, _file):
        self.file = _file
        self.fd = _file.fileno()
        self.buffer = b""
    def readinto(self, b):
        if not b:
            return 0
        n = len(b)
        if len(self.buffer) >= n:
            b[:n] = self.buffer[:n]
            self.buffer = self.buffer[n:]
            return n
        n = n - len(self.buffer)
        b[:len(self.buffer)] = self.buffer
        self.buffer = b""
        while n > 0:
            try:
                b2 = os.read(self.fd, n)
            except OSError as e:
                if e.errno != errno.EINTR:
                    raise
                continue
            if not b2:
                return len(b) - n
            n2 = len(b2)
            if n2 > n:
                self.buffer = b2[n:]
                n2 = n
           
