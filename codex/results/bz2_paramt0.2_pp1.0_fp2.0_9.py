from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 压缩数据
data = b'Lots of data here'
with BZ2File('data.bz2', 'wb') as f:
    f.write(data)

# 解压缩数据
with BZ2File('data.bz2', 'rb') as f:
    print(f.read())

# 压缩数据
data = b'Lots of data here'
with BZ2File('data.bz2', 'wb', compresslevel=9) as f:
    f.write(data)

# 解压缩数据
with BZ2File('data.bz2', 'rb') as f:
    print(f.read())

# 压缩数据
data = b'Lots of data here'
with BZ2File('data.bz2', 'wb') as f:
    f.write(data)

#
