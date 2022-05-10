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
    def readinto(self, b):
        return self.file.readinto(b)

f = File('test.txt')
f.open()
print(f.readinto(b'123'))
f.close()

# 实现一个类，它的实例可以作为上下文管理器
class ContextManager:
    def __init__(self, name):
        self.name = name
        self.file = None
    def __enter__(self):
        self.file = open(self.name, 'rb')
        return self.file
    def __exit__(self, exc_type, exc_val, exc_
