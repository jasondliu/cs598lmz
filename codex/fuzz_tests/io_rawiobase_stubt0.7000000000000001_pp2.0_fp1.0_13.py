import io
class File(io.RawIOBase):
    def __init__(self, name):
        self.name = name
        self._fd = os.open(name, os.O_RDONLY)
    def read(self, n=-1):
        if n == -1:
            return os.read(self._fd, os.path.getsize(self.name))
        else:
            return os.read(self._fd, n)
    def close(self):
        os.close(self._fd)
with File('/tmp/a.txt') as f:
    print(f.read())

# 定义一个类,实现上下文管理器
from contextlib import contextmanager
@contextmanager
def file_open(file_name):
    print('file open')
    yield {}
    print('file end')
with file_open('111') as f:
    print('file process')
