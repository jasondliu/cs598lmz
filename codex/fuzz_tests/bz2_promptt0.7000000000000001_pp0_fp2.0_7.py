import bz2
# Test BZ2Decompressor

data = bz2.compress(b'Python - BZIP2')

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data))
print(decompressor.decompress(data))
print(decompressor.decompress(data))

decompressor = bz2.BZ2Decompressor()
print(decompressor.decompress(data))

# Error
# decompressor.unused_data
# decompressor = bz2.BZ2Decompressor()
# decompressor.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x
