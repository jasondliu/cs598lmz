from bz2 import BZ2Decompressor
BZ2Decompressor()

__all__ = [
    'Decompressor',
    'GzipDecompressor',
    'DeflateDecompressor',
    'BZ2Decompressor',
    'LZMADecompressor',
    'LZWDecompressor',
    'LZMACompressor',
    'LZWCompressor',
    'ZlibDecompressor',
    'ZlibCompressor',
]

# Define an alias for the old name.
Compressor = ZlibCompressor
