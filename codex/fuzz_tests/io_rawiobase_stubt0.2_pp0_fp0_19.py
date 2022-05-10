import io
class File(io.RawIOBase):
    def __init__(self, path, mode='r'):
        self.path = path
        self.mode = mode
        self.fd = None
        self.open()

    def open(self):
        self.fd = os.open(self.path, os.O_RDONLY)

    def close(self):
        if self.fd is not None:
            os.close(self.fd)
            self.fd = None

    def readable(self):
        return True

    def readinto(self, b):
        return os.read(self.fd, b)

    def __del__(self):
        self.close()

f = File('/etc/passwd')
print(f.read(10))
f.close()

# 可以使用类似于文件的方式来操作网络流
import socket
class Network(io.RawIOBase):
    def __init__(self, host, port):
        self.host = host
       
