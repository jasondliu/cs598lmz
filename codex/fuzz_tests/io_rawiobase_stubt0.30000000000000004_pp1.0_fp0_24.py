import io
class File(io.RawIOBase):
    def __init__(self, file_name):
        self.file_name = file_name
        self.file = None
    def open(self):
        self.file = open(self.file_name, 'rb')
    def close(self):
        if self.file:
            self.file.close()
            self.file = None
    def readinto(self, b):
        return self.file.readinto(b)
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, *args):
        self.close()

with File('/tmp/file.txt') as f:
    print(f.read())

# 上下文管理器的另一个常见用途是实现一个事务或者其他的操作序列。
# 例如，下面是一个简单的数
