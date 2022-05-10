import bz2
# Test BZ2Decompressor
# data = b'BZh91AY&SY.\xc9\x8e\x1f\x00\x00\u0003\u0013IS\x80\x05\x89\tAThe quick brown fox jumped over a lazy dog.'
# decompressor = bz2.BZ2Decompressor()
# result = decompressor.decompress(data)
# print(result)
# print(decompressor.unused_data)
#
# # Test BZ2Compressor
# data = b'The quick brown fox jumped over a lazy dog.'*50
# compress = bz2.BZ2Compressor()
# print(compress.compress(data))   # initial_bytes: 0
print(compress.flush())
print(bz2.compress(data))


print(bz2.decompress(bz2.compress(data)))

# The bzip2 module also supports streaming via the BZ2Compressor and BZ2Decompressor
# classes, as well as compressing streams through the open() context manager. This
