import lzma
# Test LZMADecompressor

data = b"".join(b"%d" % i for i in range(1000))
compressed = lzma.compress(data)

decompressor = lzma.LZMADecompressor()

# Decompress data in chunks
decompressed = b""
for chunk in [compressed[:4], compressed[4:8], compressed[8:]]:
    decompressed += decompressor.decompress(chunk)

assert decompressed == data

# Decompress data in one go
decompressed = decompressor.decompress(compressed)

assert decompressed == data

# Test LZMADecompressor.flush()
decompressor = lzma.LZMADecompressor()

# Decompress data in chunks
decompressed = b""
for chunk in [compressed[:4], compressed[4:8], compressed[8:]]:
    decompressed += decompressor.decompress(chunk)

assert decompressed == data

# Decompress data in one go
decompressed = decompressor.dec
