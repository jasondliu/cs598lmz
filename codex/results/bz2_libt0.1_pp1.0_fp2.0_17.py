import bz2
bz2.decompress(bz2.compress(b'hello world!'))

# 压缩文件
with bz2.BZ2File('test.bz2', 'wb') as f:
    f.write(b'hello world!')

with bz2.BZ2File('test.bz2', 'rb') as f:
    print(f.read())

# 压缩文件
with gzip.open('test.gz', 'wb') as f:
    f.write(b'hello world!')

with gzip.open('test.gz', 'rb') as f:
    print(f.read())

# 压缩文件
with lzma.open('test.xz', 'wb') as f:
    f.write(b'hello world!')

with lzma.open('test.xz', 'rb') as f:
    print(f.read())
