from lzma import LZMADecompressor
LZMADecompressor().decompress(src).decode('utf-8')

# 或者更简单的
# bz2.decompress(src)


# bz2
import bz2
compressed = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
bz2.decompress(compressed)    # 输出: b'Wikipedia'
bz2.decompress(compressed).decode('utf-8')
