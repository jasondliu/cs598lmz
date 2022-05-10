from lzma import LZMADecompressor
LZMADecompressor.decompress(compressed_data)

# 0.6.0
from lzma import LZMAError
with open(filename, 'rb') as f:
    compressed_data = f.read()
try:
    decompressed_data = LZMADecompressor().decompress(compressed_data)
except LZMAError:
    print(filename, 'is not in the LZMA format')
else:
    print(filename, 'is valid, and the decompressed data length is',
          len(decompressed_data))

# 0.7.0
from lzma import LZMAError
with open(filename, 'rb') as f:
    compressed_data = f.read()
try:
    decompressed_data = LZMADecompressor().decompress(compressed_data)
except LZMAError as e:
    print(filename, 'is not in the LZMA format:', e)
else:
    print(filename, 'is valid, and the decompressed data length is',
          len(decompressed_data
