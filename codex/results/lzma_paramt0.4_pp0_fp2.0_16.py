from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# compress
from lzma import LZMACompressor
compressor = LZMACompressor()
compressor.compress(b'Some data')
compressor.flush()

# compress to file
from lzma import LZMAFile
with LZMAFile('file.xz', 'w') as f:
    f.write(b'Some data')

# decompress from file
from lzma import LZMAFile
with LZMAFile('file.xz', 'r') as f:
    print(f.read())

# compress to file with preset
from lzma import LZMAFile
with LZMAFile('file.xz', 'w', preset=9) as f:
    f.write(b'Some data')

# decompress from file with preset
from lzma import LZMAFile
with LZMAFile('file.xz', 'r', preset=9) as f:
    print(f.read())

# compress to file with filters
from lzma import LZMAFile
