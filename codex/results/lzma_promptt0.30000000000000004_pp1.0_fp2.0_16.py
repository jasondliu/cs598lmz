import lzma
# Test LZMADecompressor

compressor = lzma.LZMACompressor()

data = b"Hello, world!"
compressed = compressor.compress(data)
compressed += compressor.flush()

decompressor = lzma.LZMADecompressor()
decompressed = decompressor.decompress(compressed)

print(decompressed)

# Test LZMAFile

with lzma.open("test.xz", "w") as f:
    f.write(b"Hello, world!")

with lzma.open("test.xz", "r") as f:
    print(f.read())

# Test LZMAError

try:
    lzma.LZMADecompressor().decompress(b"\x00")
except lzma.LZMAError as e:
    print(e)

# Test LZMAStreamInfo

info = lzma.LZMAStreamInfo(lzma.FORMAT_RAW, lzma.CHECK_CRC64,
                           lz
