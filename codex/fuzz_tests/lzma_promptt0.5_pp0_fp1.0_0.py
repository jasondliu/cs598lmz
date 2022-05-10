import lzma
# Test LZMADecompressor

text = b"Hello world! " * 1000

comp = lzma.LZMACompressor()
compressed = comp.compress(text)
compressed += comp.flush()

decomp = lzma.LZMADecompressor()
decompressed = decomp.decompress(compressed)

assert decompressed == text
# Test LZMADecompressor.multi_decompress

text = b"Hello world! " * 1000

comp = lzma.LZMACompressor()
compressed = comp.compress(text)
compressed += comp.flush()

decomp = lzma.LZMADecompressor()
decompressed = decomp.multi_decompress(compressed)

assert decompressed == text
# Test LZMADecompressor.multi_decompress with multiple chunks

text = b"Hello world! " * 1000

comp = lzma.LZMACompressor()
compressed = comp.compress(text)
compressed += comp.flush()

decomp = lzma
