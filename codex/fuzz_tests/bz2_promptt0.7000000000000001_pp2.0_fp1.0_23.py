import bz2
# Test BZ2Decompressor

bz2data = bz2.BZ2Compressor().compress(b"Hello, world!")

bz2data += bz2.BZ2Compressor().flush()

bz2data += bz2.BZ2Compressor().compress(b"Hello 2, world!")

bz2data += bz2.BZ2Compressor().flush()

bz2data += bz2.BZ2Compressor().compress(b"Hello 3, world!")

bz2data += bz2.BZ2Compressor().flush()

print(bz2data)

print(bz2.BZ2Decompressor().decompress(bz2data))

print(bz2.BZ2Decompressor().flush())

print(bz2.BZ2Decompressor().decompress(bz2data))

print(bz2.BZ2Decompressor().flush())

print(bz2.BZ2Decompressor().decompress(bz2data))

