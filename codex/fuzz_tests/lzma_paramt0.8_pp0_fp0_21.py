from lzma import LZMADecompressor
LZMADecompressor(lzma_stream=b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\x00\x00\x00\x00').decompress(data)

# 解压缩
import bz2
bz2.decompress(data)

# 解压缩
import zlib
zlib.decompress(data, -zlib.MAX_WBITS)

```
