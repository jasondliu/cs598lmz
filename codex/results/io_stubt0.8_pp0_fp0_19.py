import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
print(view)

print('-' * 20)

# 创建字符串io
s = io.StringIO()
s.write('hello\n')
value = s.getvalue()
print(value)

print('-' * 20)

# 用指定的字符串初始化io
s = io.StringIO('hello\n world\n')
print(s.read(4))
print(s.read())
print(s.read())

print('-' * 20)

# 用文件和io操作文件名
with io.open('test.txt', 'w', encoding='utf-8') as f:
    f.write('hello world\n')

with io.open('test.txt', encoding='utf-8') as f:
    print(f.read())

print('-' * 20)

# 用文件对象的readinto方法
