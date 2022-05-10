from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# Output: b'Hello World!\n'

# Compress data
compressor = LZMACompressor()
data = b'Hello World!\n'
compressed = bytearray()
while True:
    chunk = data[:1024]
    if not chunk:
        break
    data = data[1024:]
    compressed.extend(compressor.compress(chunk))
compressed.extend(compressor.flush())

# Decompress data
decompressor = LZMADecompressor()
decompressed = bytearray()
while True:
    chunk = compressed[:1024]
    if not chunk:
        break
    compressed = compressed[1024:]
    decompressed.extend(decompressor.decompress(chunk))


