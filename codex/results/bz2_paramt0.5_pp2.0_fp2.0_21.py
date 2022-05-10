from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 压缩数据
compressor = BZ2Compressor()
for data in [b'Is there life on Mars?',
             b'Is there life on Mars?',
             b'Is there life on Mars?']:
    print(compressor.compress(data))
print(compressor.flush())

# 压缩文件
import os
from bz2 import BZ2File
with BZ2File('example.bz2', 'wb') as output:
    with open('example.txt', 'rb') as input:
        output.write(input.read())

with BZ2File('example.bz2', 'rb') as input:
    print(input.read())
os.remove('example.bz2')

# 压缩和解压缩
import bz2
uncompressed = b'We wish to inform you that we have blown up the moon.'
compressed = bz2.compress(uncompressed
