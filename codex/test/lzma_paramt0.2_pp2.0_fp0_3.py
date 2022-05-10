from lzma import LZMADecompressor
LZMADecompressor().decompress(b'\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00!\x01\x16\x00\x00\x00')

# Output: b'hello'

# Compress data
import lzma
with lzma.open('file.xz', 'w') as f:
    f.write(b'hello world')

# Decompress data
import lzma
with lzma.open('file.xz') as f:
    file_content = f.read()

# Compress data
import lzma
data = b'Lots of data here'
compressed = lzma.compress(data)

# Decompress data
import lzma
data = b'Lots of data here'
compressed = lzma.compress(data)
decompressed = lzma.decompress(compressed)

# Compress data
import lzma
