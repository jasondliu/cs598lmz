import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
decompressor.decompress(compressed)

# Test LZMACompressor
compressor = lzma.LZMACompressor()
compressor.compress(b"Hello, world!")
compressor.flush()

# Test LZMAFile
with lzma.open("/tmp/foo.xz", "w") as f:
    f.write(b"Hello, world!")

with lzma.open("/tmp/foo.xz", "r") as f:
    print(f.read())

# Test LZMAError
try:
    lzma.LZMADecompressor().decompress(b"foo")
except lzma.LZMAError as e:
    print(e)

# Test LZMAFilter
filter = lzma.LZMAFilter(lzma.FORMAT_XZ, lzma.CHECK_CRC64,
                         filters=[{"id": lzma.FILTER_LZMA2
