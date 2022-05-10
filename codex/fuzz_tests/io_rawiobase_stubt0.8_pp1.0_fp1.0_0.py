import io
class File(io.RawIOBase):
    def __init__(self, name, mode='r'):
        self.real = open(name, mode)
    def close(self):
        print('close')
        self.real.close()
    def write(self, data):
        print('write')
        self.real.write(data)
    def read(self):
        print('read')
        return self.real.read()

with File('test.txt', 'w') as f:
    f.write('abc')

with File('test.txt') as f:
    print(f.read())

f = File('test.txt')
print(f.read())

f.close()

# 命名关键字参数 a='1', b='2', c='3'
# 形参不能重复
# 默认参数 a=1
# *args 可变位置参数
# **kwargs 可变关键
