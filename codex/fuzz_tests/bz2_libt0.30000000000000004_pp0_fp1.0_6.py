import bz2
bz2.decompress(data)

# 打开一个bz2文件
with bz2.open('file.bz2', 'rt') as f:
    text = f.read()

# 打开一个gzip文件
with gzip.open('file.gz', 'rt') as f:
    text = f.read()

# 压缩数据
data = b'Lots of data here'
with gzip.open('file.gz', 'wt') as f:
    f.write(data)

# 压缩数据
data = b'Lots of data here'
with bz2.open('file.bz2', 'wt') as f:
    f.write(data)

# 压缩数据
data = b'Lots of data here'
with bz2.open('file.bz2', 'wt', compresslevel=9) as f:
    f.write(data)

# 压
