import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        self.name = name
        self.mode = mode
        self.file = None
    def __enter__(self):
        self.file = open(self.name, self.mode)
        return self
    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
    def read(self, size=-1):
        return self.file.read(size)
    def write(self, b):
        self.file.write(b)
        return len(b)
    def close(self):
        self.file.close()

with File('test.txt', 'w') as f:
    f.write('hello world')

# 上下文管理器的其他用法
# 上下文管理器的另一个用法是将它们用作装饰器。
# 
