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
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.close()
    def __repr__(self):
        return '<File name={!r}>'.format(self.name)

with File('/etc/passwd') as f:
    print(f.read(10))

# 实现上下文管理器的类通常还会实现__enter__和__exit__方法的另外两
