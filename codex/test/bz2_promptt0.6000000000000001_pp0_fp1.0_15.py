import bz2
# Test BZ2Decompressor

bz2.decompress(bz2.compress(b"Hello world"))

# Test BZ2Compressor

bz2.compress(b"Hello world")
# Test BZ2File

