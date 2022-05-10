from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(bytes(data, 'utf-8')))

# bz2.decompress(bz2.compress(bytes(data, 'utf-8')))
# bz2.decompress(bz2.compress(data))

# BZ2Decompressor().decompress(bz2.compress(bytes(data, 'utf-8')))
# BZ2Decompressor().decompress(bz2.compress(data))

# bz2.decompress(bz2.compress(bytes(data, 'utf-8')))
# bz2.decompress(bz2.compress(data))
# bz2.BZ2Compressor().flush()
# bz2.BZ2Compressor().flush(length)
# bz2.BZ2Decompressor().flush()
# bz2.BZ2Decompressor().flush(length)
# bz2.compress(data, compresslevel=9)
# bz2.decompress
