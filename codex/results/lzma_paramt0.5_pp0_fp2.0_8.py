from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# To compress data, use the compress() method.
# This returns a bytes object containing compressed data:

compressor = LZMACompressor()
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
compressed = compressor.compress(data)
compressed

# More data can be compressed by making additional calls to the compress() method:

compressor.compress(b'another chunk of data')
compressor.flush()

# The flush() method returns any remaining compressed data,
# and should always be called before discarding the compressor object:

compressor = LZMACompressor()
compressor.compress(b'First chunk of data.')
compressor.compress(b'Second chunk of data.')
compressor.flush()

#
