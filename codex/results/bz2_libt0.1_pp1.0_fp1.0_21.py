import bz2
bz2.decompress(bz2.compress(b'hello world'))

# 压缩文件
with bz2.BZ2File('test.bz2', 'wb') as f:
    f.write(b'hello world')

with bz2.BZ2File('test.bz2', 'rb') as f:
    print(f.read())

# 压缩文件
with open('test.txt', 'rb') as f:
    data = f.read()

with bz2.BZ2File('test.bz2', 'wb') as f:
    f.write(data)

# 解压文件
with bz2.BZ2File('test.bz2', 'rb') as f:
    data = f.read()

with open('test.txt', 'wb') as f:
    f.write(data)

# 压缩文件
with open('test.txt', 'rb') as f:

