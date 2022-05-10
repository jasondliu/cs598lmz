from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(file)

# bz2.compress/decompress not supported

# lzma Module
# LZMA crunches based on LZ77 algorithm. Offers best compression ratio and better compression rate
# LZMA compression level is based on two parameters - the compression level (1 - 9) and dict_size( 16, 32, 64, 256, 1024, 4096, 8192, 16384, 65536, 2097152) 
# lzma module implements both compression and decompression
from lzma import compress, decompress
str = b'No compresssion0'
compress(str) 
b'x\x9c]\xdbX\xcbO\xcf\xf7\n\xc40\x14\x00\x00\x11*\x01\xcc'
# Note: compressed string cannot be decoded with text or base64 module
decompress(b'x\x9c]\xdbX\xcbO\xcf\xf7\n\xc40\x14\x00\x00\x11*\x
