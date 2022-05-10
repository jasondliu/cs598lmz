import lzma
# Test LZMADecompressor
compressed = lzma.compress(b"Hello world!")
decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)
print(decompressed)

# Test LZMACompressor
compressor = lzma.LZMACompressor()
compressed = compressor.compress(b"Hello world!")
compressed += compressor.flush()
print(compressed)

# Test LZMAFile
with open("lzma_file.lzma", "wb") as f:
    f.write(lzma.compress(b"Hello world!"))

with lzma.open("lzma_file.lzma") as f:
    print(f.read())

with lzma.open("lzma_file.lzma", "rt") as f:
    print(f.read())

# Test LZMAError
try:
    lzma.decompress(b"bad data")
except lzma.LZMAError as e
