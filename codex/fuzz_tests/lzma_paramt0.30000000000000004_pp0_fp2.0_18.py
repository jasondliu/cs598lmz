from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# 使用lzma压缩
from lzma import LZMACompressor
compressor = LZMACompressor()
compressor.compress(b'Hello World!')
compressor.flush()

# 使用bz2压缩
import bz2
bz2.compress(b'Hello World!')

# 使用bz2解压缩
bz2.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x
