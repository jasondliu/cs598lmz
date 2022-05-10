import bz2
bz2.decompress(data)

# 使用bz2.BZ2Decompressor对象解压数据
d = bz2.BZ2Decompressor()
d.decompress(data)

# 同时读取压缩和解压数据
data = bz2.compress(b'hello world')
with open('bz2_compress.bz2', 'wb') as f:
    f.write(data)

with open('bz2_compress.bz2', 'rb') as f:
    data = f.read()
    print(data)

with bz2.open('bz2_compress.bz2', 'rb') as f:
    data = f.read()
    print(data)

# 压缩文件
with open('bz2_compress.bz2', 'wb') as f:
    f_compress = bz2
