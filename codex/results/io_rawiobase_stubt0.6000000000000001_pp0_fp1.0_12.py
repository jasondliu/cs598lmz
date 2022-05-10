import io
class File(io.RawIOBase):
    def write(self, data):
        print('write:', data)
    def read(self, size=-1):
        print('read:', size)
        return b'abc'
    def readable(self):
        return True
    def writable(self):
        return True
f = File()
f.write(b'hello')
f.read()

# 可以通过继承 io.TextIOBase 来实现文本文件

# 文件上下文管理器
# 文件对象支持上下文管理器协议，可以使用 with 语句来自动关闭文件

with open('test.txt', 'w') as f:
    f.write('hello world')

# 文本文件
# 对于
