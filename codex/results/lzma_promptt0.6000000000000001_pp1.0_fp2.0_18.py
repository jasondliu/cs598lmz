import lzma
# Test LZMADecompressor.decompress() with a data stream that's a little
# longer than the internal buffer of the decompressor.

compressed = lzma.compress(b"Hello world!")

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
decompressed += decompressor.flush()

assert decompressed == b"Hello world!"

# Test with multiple calls to decompress(), each of which provides a
# portion of the data stream.

decompressor = lzma.LZMADecompressor()

decompressed = decompressor.decompress(compressed[:4])

decompressed += decompressor.decompress(compressed[4:8])

decompressed += decompressor.decompress(compressed[8:12])

decompressed += decompressor.decompress(compressed[12:16])

decompressed += decompressor.decompress(compressed[16:])

decompressed += decompressor.flush()

assert decompressed == b"
