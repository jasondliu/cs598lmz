import lzma
# Test LZMADecompressor

comp = lzma.LZMACompressor()

data = b"hello world! " * 1000

compressed = comp.compress(data)
compressed += comp.flush()

decomp = lzma.LZMADecompressor()
decompressed = decomp.decompress(compressed)

print(len(compressed), len(decompressed))
assert decompressed == data

# Test LZMADecompressor.decompress() with multiple calls

decomp = lzma.LZMADecompressor()

decompressed = decomp.decompress(compressed[:30])
decompressed += decomp.decompress(compressed[30:])

assert decompressed == data

# Test LZMADecompressor.decompress() with multiple calls and max_length

decomp = lzma.LZMADecompressor()

decompressed = decomp.decompress(compressed[:30], max_length=10)
