import bz2
bz2.decompress(bz2.compress(b'hello world'))

# 压缩文件
with bz2.BZ2File('file.bz2', 'wb') as f:
    f.write(b'hello world')

with bz2.BZ2File('file.bz2', 'rb') as f:
    print(f.read())

# 压缩文件
with gzip.open('file.gz', 'wb') as f:
    f.write(b'hello world')

with gzip.open('file.gz', 'rb') as f:
    print(f.read())

# 压缩文件
with lzma.open('file.xz', 'wb') as f:
    f.write(b'hello world')

with lzma.open('file.xz', 'rb') as f:
    print(f.read())
