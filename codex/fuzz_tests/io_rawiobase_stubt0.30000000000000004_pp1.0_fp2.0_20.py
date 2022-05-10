import io
class File(io.RawIOBase):
    def __init__(self, path):
        self.path = path
        self.file = None
    def open(self):
        self.file = open(self.path, 'rb')
    def read(self, size=-1):
        return self.file.read(size)
    def close(self):
        self.file.close()
    def __enter__(self):
        self.open()
        return self
    def __exit__(self, *args):
        self.close()

with File('/tmp/file.txt') as file:
    print(file.read())

# 上面的代码中，File类实现了上下文管理器，它的open()方法打开文件，close()方法关闭文件，
# 这样就不需要显式的调用open()和close()方
