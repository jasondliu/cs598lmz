import bz2
bz2.decompress(bz2.compress(b'hello world!'))

# 将压缩后的数据写入到文件对象中
with open('example.bz2', 'wb') as f:
    f.write(bz2.compress(b'hello world!'))

# 将压缩后的数据读取出来
with open('example.bz2', 'rb') as f:
    print(bz2.decompress(f.read()))

# 压缩文件
with bz2.BZ2File('example.bz2', 'wb') as f:
    f.write(b'hello world!')

# 解压文件
with bz2.BZ2File('example.bz2', 'rb') as f:
    print(f.read())
