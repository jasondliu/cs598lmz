import lzma
lzma_compressor = lzma.LZMACompressor()

def compress_lzma(data):
    """Compress data using lzma compression."""
    return lzma_compressor.compress(data)

def decompress_lzma(data):
    """Decompress data using lzma compression."""
    return lzma.decompress(data)


# Bzip2
import bz2
bz2_compressor = bz2.BZ2Compressor()

def compress_bz2(data):
    """Compress data using bz2 compression."""
    return bz2_compressor.compress(data)

def decompress_bz2(data):
    """Decompress data using bz2 compression."""
    return bz2.decompress(data)


# Zlib
import zlib
def compress_zlib(data):
    """Compress data using zlib compression."""
    return zlib.compress(data)

