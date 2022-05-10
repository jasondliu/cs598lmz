from lzma import LZMADecompressor
LZMADecompressor().decompress(data)
b'This is the text to be compressed.\n'

# To decompress a single file, use the LZMAFile class:
from lzma import LZMAFile
f = LZMAFile('lorem.lzma')
print(f.read())

# To compress data in memory, use the compress() function:
from lzma import compress
print(compress(b'This is the text to be compressed.'))

# To decompress data in memory, use the decompress() function:
from lzma import decompress
print(decompress(b'...'))

# To compress data incrementally, use the LZMACompressor class:
from lzma import LZMACompressor
compressor = LZMACompressor()
compressor.compress(b'Some data')
compressor.compress(b'Some more data')
compressor.flush()
b'...'

# To decompress data incrementally, use the LZMADecompressor class:
from lzma import LZMADecompressor
