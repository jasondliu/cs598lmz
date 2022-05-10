import bz2
bz2.decompress()

# 读写非文本文件
with open('somefile.bin', 'rb') as f:
    data = f.read()

# 写二进制数据到文本文件
with open('somefile.bin', 'rb') as f:
    data = f.read()
with open('somefile.txt', 'wt') as f:
    f.write(data)

# 对于非文本文件，使用b模式打开
f = open('bfile', 'wb')
f.write(b'Hello World')

# 将一个文本文件读取到一个字符串中
with open('hello.txt', 'rt') as f:
    data = f.read()

# 将一个二进制文件读取
