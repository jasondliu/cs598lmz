import bz2
# Test BZ2Decompressor.flush() behavior

data = bz2.compress(b'a' * 50)

decompressor = bz2.BZ2Decompressor()

decompressor.decompress(data[:10])
