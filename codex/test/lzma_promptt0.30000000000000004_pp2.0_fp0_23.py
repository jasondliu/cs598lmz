import lzma
# Test LZMADecompressor

compressor = lzma.LZMACompressor()

data = b"Hello world! " * 1000
compressed = compressor.compress(data)
compressed += compressor.flush()

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)

print(decompressed == data)

# Test LZMAFile

with lzma.open("hello.xz", "w") as f:
    f.write(data)

with lzma.open("hello.xz", "r") as f:
    print(f.read() == data)

# Test LZMAError

try:
    lzma.decompress(b"")
except lzma.LZMAError as e:
    print(e.args[0] == "Couldn't find end of stream marker")

