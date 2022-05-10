import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.f = open(filename, mode)
    def read(self, n):
        return self.f.read(n)
    def write(self, b):
        self.f.write(b)
    def close(self):
        self.f.close()
    def __enter__(self):
        return self
    def __exit__(self, *args):
        self.close()

with File('file.txt', 'w') as f:
    f.write('hello world')

# 上面的代码可以用下面的代码替换，使用了 contextlib 模块中的 contextmanager 装饰器
from contextlib import contextmanager

@contextmanager
def file(filename, mode):
    f = open(filename, mode)
    try:
        yield f
    finally:
        f.close()

with file('file.txt', '
