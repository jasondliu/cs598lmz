from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

import zlib
decompressor = zlib.decompressobj()
decompressor.decompress(compressed_data)
decompressor.flush()

import bz2
compressor = bz2.BZ2Compressor()
compressor.compress(b'x' * 1048576)
compressor.flush()

decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed_data)
decompressor.decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
decompressor.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x
