from lzma import LZMADecompressor
LZMADecompressor.__new__.__defaults__


# LZMACompressor
import binascii
from lzma import LZMACompressor
comp = LZMACompressor()
len(comp.compress(b'Test')) # compressed output length
comp.flush()
len(comp.compress(b'Test')) # compressed output length

# LZMADecompressor
from lzma import LZMADecompressor
decomp = LZMADecompressor()
decomp.decompress(comp.compress(b'Test'))
decomp.unused_data
decomp.decompress(comp.flush())

# LZMADecompressor.decompress(data)
# LZMADecompressor.unconsumed_tail
# LZMADecompressor.unused_data
# LZMADecompressor.eof

# LZMAFile
from lzma import LZMAFile
f = LZMAFile('lzma_compressed', 'w', format=FORMAT_XZ)
