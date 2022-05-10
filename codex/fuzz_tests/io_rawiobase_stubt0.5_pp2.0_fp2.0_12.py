import io
class File(io.RawIOBase):
    def __init__(self, fd):
        self.fd = fd
    def readinto(self, buf):
        return os.read(self.fd, buf)
    def close(self):
        os.close(self.fd)

# f = File(os.open('/etc/passwd', os.O_RDONLY))
# print(f.read())

# f = open('/etc/passwd', 'rb')
# print(f.read())

class BufferedReader(io.RawIOBase):
    def __init__(self, raw):
        self.raw = raw
        self.buffer = b''
    def readinto(self, buf):
        n = len(buf)
        while len(self.buffer) < n:
            chunk = self.raw.read(n - len(self.buffer))
            if not chunk:
                break
            self.buffer += chunk
        n = min(n, len(self.buffer))
        buf[:n] = self.buffer[:n]
        self.buffer = self
