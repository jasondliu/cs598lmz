from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 压缩数据
data = b'Lots of data here'
compressor = BZ2Compressor()
compressor.compress(data)
compressor.flush()

# 压缩文件
import bz2
with open('filename.txt', 'rb') as input:
    with bz2.open('filename.txt.bz2', 'wb') as output:
        output.write(input.read())

# 解压文件
import bz2
with bz2.open('filename.txt.bz2', 'rb') as input:
    with open('filename.txt', 'wb') as output:
        output.write(input.read())

# 压缩和解压字符串
import bz2
original_data = b'This is the original text.'
print('Original     :', len(original_data), original_data)
compressed = bz2.compress(
