import lzma
# Test LZMADecompressor

compressor = lzma.LZMACompressor()
decompressor = lzma.LZMADecompressor()

data = b"Hello world! " * 100

compressed = compressor.compress(data)

decompressed = decompressor.decompress(compressed)

print(decompressed)

# Test LZMAFile

with lzma.open("test.xz", "w") as f:
    f.write(data)

with lzma.open("test.xz", "r") as f:
    print(f.read())

# Test LZMAError

try:
    decompressor.decompress(b"")
except lzma.LZMAError as e:
    print("Got an exception:", e)

# Test LZMAStream

compressor = lzma.LZMACompressor()

compressor.compress(b"Hello ")
compressor.compress(b"world!")

print(compressor.flush())

# Test LZMA
