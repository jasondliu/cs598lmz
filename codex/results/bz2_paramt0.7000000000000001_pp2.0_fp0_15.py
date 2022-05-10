from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# It's also possible to compress data in memory using a BZ2Compressor object.
# The BZ2Compressor.compress() method can be repeatedly called with chunks of data and the compressor object will
# return chunks of compressed data. When you are finished compressing data, call the BZ2Compressor.flush() method
# to flush any remaining compressed data.
# The following example uses BZ2Compressor to compress a few blocks of data:
from bz2 import BZ2Compressor
compressor = BZ2Compressor()
compressor.compress(b'Hello')
compressor.compress(b' ')
compressor.compress(b'World')
compressor.flush()

# The zlib module provides
