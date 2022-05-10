import bz2
bz2.decompress(data)

# 打开文件
f = bz2.open('file.txt.bz2', 'wt')
f.write('hello world')
f.close()

# 压缩
data = bz2.compress(b'hello world')
data

# 解压
bz2.decompress(data)

# 压缩文件
f = bz2.open('file.txt.bz2', 'wt')
f.write('hello world')
f.close()

# 解压文件
f = bz2.open('file.txt.bz2', 'rt')
f.read()

# 压缩文件
with bz2.open('file.txt.bz2', 'wt') as f:
    f.write('hello world')

# 解压文件
with bz2.open('file.txt.bz2', 'rt') as f:
