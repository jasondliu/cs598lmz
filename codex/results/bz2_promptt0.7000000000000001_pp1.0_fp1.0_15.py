import bz2
# Test BZ2Decompressor

data = b"".join([bytes([i]) * i for i in range(1, 256)])
data = bz2.compress(data)
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(data)

# Test BZ2Compressor

compressor = bz2.BZ2Compressor()
compressor.compress(data)
compressor.flush()
