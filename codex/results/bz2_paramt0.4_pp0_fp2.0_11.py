from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# 在一个线程中运行压缩数据
from bz2 import BZ2Compressor
compressor = BZ2Compressor()
compressor.compress(b'x' * 10)
compressor.flush()

# 压缩文件
with open('file.txt', 'rb') as input:
    with bz2.open('file.txt.bz2', 'wb') as output:
        output.writelines(input)

# 解压文件
with bz2.open('file.txt.bz2', 'rb') as input:
    with open('file.txt', 'wb') as output:
        output.writelines(input)

# 压缩数据流
import bz2
compressor = bz2.BZ2Compressor()
compressor.compress(b'hello world!')
compressor.flush()

# 解压
