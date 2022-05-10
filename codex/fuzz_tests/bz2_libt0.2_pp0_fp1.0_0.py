import bz2
bz2.decompress(bz2.compress(b'hello world!'))

# 压缩文件
with bz2.BZ2File('spam.bz2', 'wb') as f:
    f.write(b'Hello World!')

# 解压文件
with bz2.BZ2File('spam.bz2', 'rb') as f:
    print(f.read())
