from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 压缩数据
data = b'Lots of data here'
compressor = BZ2Compressor()
compressor.compress(data)
compressor.flush()

# 使用压缩文件
import bz2
with bz2.open('file.bz2', 'wt') as f:
    f.write(data)

with bz2.open('file.bz2', 'rt') as f:
    print(f.read())

# 压缩文件
import bz2
with open('file.txt', 'rb') as input:
    with bz2.open('file.bz2', 'wb') as output:
        output.writelines(input)

# 解压文件
import bz2
with bz2.open('file.bz2', 'rb') as input:
    with open('file.txt', 'wb') as output:
        output.writelines
