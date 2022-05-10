import bz2
bz2.decompress(bz2_data)

# 打开二进制文件
f = open('somefile.bin', 'rb')
chunk = f.read(16)
chunk

# 使用bz2压缩数据
with open('somefile.bin', 'rb') as f:
    data = f.read()

compressed = bz2.compress(data)

# 将压缩后的数据写入文件
with open('somefile.bz2', 'wb') as f:
    f.write(compressed)

# 将压缩后的数据写入文件
with open('somefile.bz2', 'wb') as f:
    f.write(compressed)

# 读取压缩文件
with open('somefile.bz2', 'rb') as f:
    decomp
