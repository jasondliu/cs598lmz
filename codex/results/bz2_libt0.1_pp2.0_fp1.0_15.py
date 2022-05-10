import bz2
bz2.decompress(bz2.compress(b'hello world'))

# 压缩文件
with bz2.open('file.bz2', 'wt') as f:
    f.write('hello world')

with bz2.open('file.bz2', 'rt') as f:
    print(f.read())

# 压缩文件
with gzip.open('file.gz', 'wt') as f:
    f.write('hello world')

with gzip.open('file.gz', 'rt') as f:
    print(f.read())

# 压缩文件
with lzma.open('file.xz', 'wt') as f:
    f.write('hello world')

with lzma.open('file.xz', 'rt') as f:
    print(f.read())
