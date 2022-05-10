from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(b'hello world!'))

# 压缩数据
import bz2
uncompressed_data = b'Hello World!Hello World!Hello World!Hello World!'
compressed_data = bz2.compress(uncompressed_data)
print(compressed_data)

# 解压缩数据
import bz2
compressed_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
uncompressed_data = bz2.decompress(compressed_data)
print(uncompressed_data)

# 压缩文件
import bz2
with open('somefile.txt', 'rb') as input:
    compressed
