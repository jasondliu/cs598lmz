import lzma
# Test LZMADecompressor

input_size = 100000
output_size = input_size * 2

buf1 = b"".join([random.choice(b"abcdefghijklmnop") \
    for i in range(input_size)])
compressor = lzma.LZMACompressor()
buf2 = compressor.compress(buf1)
buf3 = compressor.flush()
compressor = lzma.LZMADecompressor()
buf4 = compressor.decompress(buf2 + buf3)

if sys.version_info >= (3, 0):
    assert buf1 == bytes(buf4)
else:
    assert buf1 == b"".join(buf4)
