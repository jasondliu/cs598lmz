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
    def readable(self):
        return True
    def readinto(self, b):
        return os.read(self.fd, b)

f = File('/etc/passwd')
f.open()
print(f.read())
f.close()

# 上面的代码可以改写成下面这样：
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.fd = None
    def open(self):
        self.fd = os.open(self.name, os.O_RDONLY)
    def close(
