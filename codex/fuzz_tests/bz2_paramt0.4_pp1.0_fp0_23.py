from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 压缩和解压缩数据
import bz2
uncompressed = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
compressed = bz2.compress(uncompressed)
print(compressed)
print(bz2.decompress(compressed))

# 压缩和解压缩文件
import bz2
with open('bz2_compress.py', 'rt') as input:
    with bz2.open('bz2_compress.py.bz2', 'wt') as output:
        output.write(input.read())

with bz2.open('b
