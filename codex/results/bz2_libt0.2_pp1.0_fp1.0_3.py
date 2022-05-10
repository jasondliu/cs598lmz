import bz2
bz2.decompress(bz2.compress(b'Hello World!'))

# 将压缩后的数据写入文件
with bz2.BZ2File('spam.bz2', 'wb') as f:
    f.write(b'Hello World!')

# 读取压缩文件
with bz2.BZ2File('spam.bz2', 'rb') as f:
    print(f.read())

# 压缩文件的迭代
with bz2.BZ2File('spam.bz2', 'rb') as f:
    for line in f:
        print(line)

# 压缩文件的迭代
with bz2.BZ2File('spam.bz2', 'rb') as f:
    print(f.readline())

# 压缩文件的迭代
with bz2.B
