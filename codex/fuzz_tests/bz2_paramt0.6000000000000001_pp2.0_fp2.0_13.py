from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 压缩数据
data = b'Hello World'
bz2_data = BZ2Compressor().compress(data)
bz2_data

# 解压缩数据
bz2_data
BZ2Decompressor().decompress(bz2_data)

# 压缩文件
import bz2
with open('compress.txt', 'rb') as input:
    with bz2.open('compress.bz2', 'wb') as output:
        output.writelines(input)

# 解压缩文件
import bz2
with bz2.open('compress.bz2', 'rb') as input:
    with open('uncompress.txt', 'wb') as output:
        for line in input:
            output.write(line)
