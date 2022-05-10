import bz2
# Test BZ2Decompressor

bz2_data = b'this is some text'
compressed_data = bz2.compress(bz2_data)
len(compressed_data)

decompressor = bz2.BZ2Decompressor()

decompressor.decompress(compressed_data)

decompressor.unused_data

