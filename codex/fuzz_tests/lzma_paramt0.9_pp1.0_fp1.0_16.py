from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

decompressor = LZMADecompressor()
decompressor.decompress(compressed_data)
decompressor.flush()

# max_length=100000000 is actually necessary to see if
# a malformed input is really compressed
decompressor.decompress(b'<malformed input>',
                        max_length=100000000)

LZMADecompressor(format=LZMA_FORMAT_AUTO).decompress(compressed_data)
LZMADecompressor(format=LZMA_FORMAT_RAW).decompress(compressed_data)
LZMADecompressor().decompress(compressed_data)

LZMADecompressor(format=LZMA_FORMAT_RAW).decompress(b'x\x9c' + data)
LZMADecompressor(format=LZMA_FORMAT_XZ).decompress(b'<xz header>'+data)

# LZMADecompressor objects
