import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode
        self.file = None
        self.open()

    def open(self):
        self.file = open(self.filename, self.mode)

    def read(self, size=-1):
        return self.file.read(size)

    def write(self, b):
        return self.file.write(b)

    def close(self):
        return self.file.close()

    def __del__(self):
        self.close()

f = File('/tmp/test.txt', 'wb+')
f.write(b'Hello world!')
f.close()

f = File('/tmp/test.txt', 'rb')
print(f.read())
f.close()

# 可以通过定义一个close方法来清理对象
class File(io.RawIOBase):
    def __init__(self, filename, mode):

