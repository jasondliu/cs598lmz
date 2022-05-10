import io
class File(io.RawIOBase):
    def __init__(self):
        super(File, self).__init__()
        self.f = None
    def open(self):
        self.f = open('test.txt', 'r+')
    def read(self, size=-1):
        return self.f.read(size)
    def write(self, b):
        return self.f.write(b)
    def close(self):
        self.f.close()
f = File()
f.open()
f.write(b'hello')
print(f.read(5))
f.close()
'''

# 方式二：使用 抽象基类
'''
import io
class File(io.FileIO):
    def __init__(self, filename, mode='r+'):
        super(File, self).__init__(filename, mode)
f = File('test.txt')
f.write(b'hello')
print(f.read(5))
f.close()
'''

