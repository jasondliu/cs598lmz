from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# b'Hello World\n'

# Compressing and decompressing
import lzma
data = b'Hello World'
compressed = lzma.compress(data)
print(compressed)

# b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00t/\xe5\xa3\x01\x00\x04]'

decompressed = lzma.decompress(compressed)
print(decompressed)

# b'Hello World'

# Specifying a preset
import lzma
data = b'Hello World'
compressed = lzma.compress(data, preset=9)
print(compressed)

# b'\xfd7zXZ\x00\x00\x04\xe6\xd6\xb4F\x02\x00!\x01\x16\x00\x00\x00
