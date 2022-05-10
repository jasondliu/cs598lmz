import bz2
bz2.decompress(bz2.compress(b'hello world!'))

# 利用bz2压缩文件
with open('test.txt', 'rb') as f:
    data = f.read()

with bz2.open('test.bz2', 'wb') as f:
    f.write(data)

with bz2.open('test.bz2', 'rb') as f:
    data = f.read()

with open('test.txt', 'wb') as f:
    f.write(data)
