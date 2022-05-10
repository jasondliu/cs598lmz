from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')

# The bz2 module provides a comprehensive interface for the bz2 compression library. It implements a complete file interface, one shot (de)compression functions, and types for sequential (de)compression.

# The BZ2Compressor and BZ2Decompressor classes provide a complete interface to compress and decompress data sequentially.

# The compress() and decompress() functions provide one-shot (de)compression.

# The BZ2File class provides a file-like interface to file objects (either strings or bytes).

# BZ2Compressor.compress()
# Compress data, returning a chunk of compressed data if possible.

# Some of the compressed data may be buffered internally, and compressed data may be returned immediately.
