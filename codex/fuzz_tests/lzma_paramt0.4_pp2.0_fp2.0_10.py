from lzma import LZMADecompressor
LZMADecompressor.decompress(data)

# 将数据压缩成一个文件对象
import io
import lzma
with open('/tmp/backup.xz', 'rb') as input, \
        lzma.open('/tmp/backup.xz', 'wt') as output:
    output.write(input.read())

# 使用LZMA算法压缩数据
import lzma
data = b'Lots of content here'
with lzma.open('/tmp/backup.xz', 'w') as f:
    f.write(data)

# 使用bz2压缩数据
import bz2
uncompressed_data = b'Lots of content here'
compressed_data = bz2.compress(uncompressed_data)
len(uncompressed_data)
len(compressed_data)

# 解压缩
