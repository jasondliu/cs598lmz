from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# Compress a stream of data
from lzma import LZMACompressor
compressor = LZMACompressor()
compressor.compress(b'Binary data')
compressor.flush()


### bz2
# Compress data
import bz2
bz2.compress(data)

# Decompress data
bz2.decompress(data)

# Compress a stream of data
compressor = bz2.BZ2Compressor()
compressor.compress(b'Binary data')
compressor.flush()

# Decompress a stream of data
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x08
