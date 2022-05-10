from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# 压缩
from bz2 import BZ2Compressor
BZ2Compressor().compress(b'hello world!hello world!hello world!')

# 压缩文件
import bz2
uncompressed = b'We are the knights who say Ni!'
with bz2.BZ2File('/tmp/uncompressed.txt', 'wb') as f:
    f.write(uncompressed)
with bz2.BZ2File('/tmp/uncompressed.txt', 'rb') as f:
    print(f.read())

# 解压缩文件
import bz2
