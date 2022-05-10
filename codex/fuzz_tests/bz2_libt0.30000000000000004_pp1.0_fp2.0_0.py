import bz2
bz2.decompress(bz2.compress(data))

# 压缩文件
with open('test.txt', 'rb') as f:
    data = f.read()
with bz2.open('test.bz2', 'wb') as f:
    f.write(data)
with bz2.open('test.bz2', 'rb') as f:
    data = f.read()
print(data)

# 压缩文件
import gzip
with open('test.txt', 'rb') as f:
    data = f.read()
with gzip.open('test.gz', 'wb') as f:
    f.write(data)
with gzip.open('test.gz', 'rb') as f:
    data = f.read()
print(data)

# 压缩文件
import lzma
with open('test.txt', 'rb') as f:
    data = f.read()
with lzma.open('test.xz', '
