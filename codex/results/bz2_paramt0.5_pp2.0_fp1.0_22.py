from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# bz2.BZ2Compressor
# bz2.BZ2Decompressor

# 使用bz2模块
# 压缩文件
import bz2

with open('bz2_compress.txt','rt') as f:
    data = f.read()

compressed = bz2.compress(data.encode('utf-8'))

with open('bz2_compress.bz2','wb') as f:
    f.write(compressed)

# 解压缩文件
import bz2

with open('bz2_compress.bz2','rb') as f:
    data = f.read()

original = bz2.decompress(data)

print(original.decode('utf-8'))
