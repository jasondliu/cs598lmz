from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

# bz2
import bz2
compressed_data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
bz2.decompress(compressed_data)

# zlib
import zlib
compressed_data = b'x\x9cK\xca\xcfM\xce\xcf\xcb\xcc\xceK\xce\xcd\x05\x00\x00\x00\x03\xf3\r\n'
zlib.decompress(compressed_data)

# lzw
import lzw
compressed_data = b'\xd2\xcd\xc9\xc9W(\xcf/\xcaIQ\xcc \x82
