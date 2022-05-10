import io
class File(io.RawIOBase):
    def __init__(self, filename):
        self.filename = filename
        self.file = None
    def open(self):
        self.file = open(self.filename, 'rb')
    def close(self):
        if self.file:
            self.file.close()
            self.file = None
    def readinto(self, b):
        return self.file.readinto(b)
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()

with File('/etc/passwd') as f:
    print(f.read(10))

# 上下文管理器的一个更复杂的例子，它演示了如何在一个类中实现上下文管理器
from socket import socket, AF_INET
