from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# 使用bz2模块压缩
data = b'Lots of data here'
import bz2
bz2.compress(data)

# 使用bz2模块压缩文件
import bz2
with open('file.txt', 'rt') as input:
    with bz2.open('file.txt.bz2', 'wt') as output:
        for line in input:
            output.write(line)

# 使用bz2模块解压文件
import bz2
with bz2.open('file.txt.bz2', 'rt') as input:
    with open('file.txt', 'wt') as output:
        for line in input:
            output.write(line)

# 使用zlib模块解压数据
import zlib
data = b'Lots of data here'
