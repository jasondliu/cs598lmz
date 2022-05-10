import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.fd = None
    def open(self):
        self.fd = os.open(self.name, os.O_RDONLY)
    def close(self):
        if self.fd is not None:
            os.close(self.fd)
            self.fd = None
    def fileno(self):
        self.open()
        return self.fd
    def readable(self):
        return True
    def readinto(self, b):
        self.open()
        return os.read(self.fd, b)
    def __del__(self):
        self.close()

f = File('/etc/passwd')
print(f.read(10))

# 实现一个文件对象，支持迭代
class FileIter:
    def __init__(self, f):
        self.f = f
    def __iter__(self):
        return self
    def
