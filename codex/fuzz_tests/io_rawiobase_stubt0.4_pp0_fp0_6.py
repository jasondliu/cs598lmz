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
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    def fileno(self):
        return self.fd
    def readable(self):
        return True
    def readinto(self, b):
        return os.read(self.fd, b)
with File('/tmp/file.txt') as f:
    print(f.read())

# 用户自定义的类，可以实现上下文管理器，只
