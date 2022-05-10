import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self.file = None
    def open(self):
        self.file = open(self.name, 'rb')
    def close(self):
        if self.file:
            self.file.close()
            self.file = None
    def readinto(self, buf):
        return self.file.readinto(buf)
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, *args):
        self.close()

with File('test.txt') as f:
    print(f.read())

# 上下文管理器的另一个常见用途是为线程锁定和解锁资源。
# 下面是一个锁定和解锁线程的例子
