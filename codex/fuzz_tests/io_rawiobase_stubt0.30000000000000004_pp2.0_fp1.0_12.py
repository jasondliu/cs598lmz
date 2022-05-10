import io
class File(io.RawIOBase):
    def __init__(self, name, mode):
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
        return self.file.write(b)
    def seek(self, offset, whence=0):
        return self.file.seek(offset, whence)
    def tell(self):
        return self.file.tell()

with File('myfile.txt', 'w') as f:
    f.write('hello')

# 实现__enter__和__exit__方法的类，称为上下文管理器。
# 上下文
