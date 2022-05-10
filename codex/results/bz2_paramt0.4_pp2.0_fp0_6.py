from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# 使用 bz2.decompress()
bz2_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
bz2.decompress(bz2_data)

# 压缩文件
import bz2
uncompressed_data = b'The same line, over and over.\n' * 10
len(uncompressed_data)

with bz2.BZ2File('uncompressed.txt', 'wb') as f:
    f.write(uncompressed_data)

with bz2.BZ2File('uncompressed.txt', 'rb') as f:
    print(f.read(100))

with bz2.BZ
