from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 创建一个压缩文件
import bz2
uncompressed_data = b'Welcome to the Idiot\'s Guide to Compression!'
with bz2.BZ2File('uncompressed.txt', 'wb') as f:
    f.write(uncompressed_data)

with bz2.BZ2File('uncompressed.txt', 'rb') as f:
    print(f.read())

# 压缩数据
compressed_data = bz2.compress(uncompressed_data)
print(compressed_data)

# 解压缩数据
print(bz2.decompress(compressed_data))

# 压缩文件
import gzip
with gzip.open('uncompressed.txt.gz', 'wt') as f:
    f.write('Contents of the example file go here.\n')

with gzip
