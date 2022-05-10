import io
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.file = open(filename, mode)
    def read(self, size=-1):
        return self.file.read(size)
    def write(self, data):
        return self.file.write(data)
    def close(self):
        return self.file.close()

file = File('test.txt', 'w')
file.write(b'Hello World')
file.close()

file = File('test.txt', 'r')
print(file.read())
file.close()

# 使用类来实现上下文管理器
class File(io.RawIOBase):
    def __init__(self, filename, mode):
        self.file = open(filename, mode)
    def read(self, size=-1):
        return self.file.read(size)
    def write(self, data):
        return self.file.write(data)
    def close(self):
        return self.file
