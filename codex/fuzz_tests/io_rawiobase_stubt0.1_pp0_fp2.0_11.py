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
        return '<File {!r}>'.format(self.name)

with File('file.txt') as f:
    print(f.read())

# 上下文管理器的另一个重要特性是它们可以被嵌套使用。
# 例如，
