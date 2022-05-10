from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# b'Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!Hello World!'

# 压缩
compressor = LZMACompressor()
compressor.compress(b'Hello World!')
compressor.compress(b'Hello World!')
compressor.compress(b'Hello World!')
compressor.compress(b'Hello World!')
compressor.compress(b'Hello World!')
compressor.compress(b'Hello World!')
compressor.compress(b'Hello World!')
compressor.compress(b'Hello World!')
compressor.compress(b'Hello World!')
compressor.compress(b'Hello World!')

compressor.flush()

# b'\xfd\xff\xff\xff\xff\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\
