import bz2
bz2.decompress(bz2.compress(b'hello world'))

# 压缩文件
with bz2.BZ2File('spam.bz2', 'wb') as f:
    f.write(b'hello world')

with bz2.BZ2File('spam.bz2', 'rb') as f:
    print(f.read())

# 压缩文件
with open('spam.bz2', 'rb') as f:
    print(bz2.decompress(f.read()))

# 压缩文件
with open('spam.bz2', 'wb') as f:
    f.write(bz2.compress(b'hello world'))

with open('spam.bz2', 'rb') as f:
    print(bz2.decompress(f.read()))

# 压缩文件
with open('spam.bz2', 'wb') as f
