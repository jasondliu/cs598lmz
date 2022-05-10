import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.fd = None
    def open(self):
        self.fd = os.open(self.path, os.O_RDONLY)
    def close(self):
        if self.fd is not None:
            os.close(self.fd)
            self.fd = None
    def fileno(self):
        return self.fd
    def readable(self):
        return True
    def readinto(self, b):
        return os.read(self.fd, b)
    def __del__(self):
        self.close()

f = File('/tmp/spam')
f.open()
print(f.read(5))
f.close()

# 如果你想编写一个上下文管理器，你需要实现上下文管理器协议。
# 这
