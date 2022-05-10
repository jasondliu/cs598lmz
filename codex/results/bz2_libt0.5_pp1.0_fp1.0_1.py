import bz2
bz2.decompress(bz2_data)

# You can also use bz2.BZ2Decompressor to decompress data incrementally.
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(bz2_data)
decompressor.decompress(more_bz2_data)
decompressor.flush()

# bz2.compress() and bz2.decompress() produce one compressed block each.
# If you want to compress data in a stream like manner, you can use a BZ2Compressor object.

compressor = bz2.BZ2Compressor()
compressor.compress(b'i am a string')
compressor.compress(b'i am another string')
compressor.flush()

# The flush() method is needed to ensure that all internal buffers are flushed.
# Otherwise, the compressed data may be missing some part of the input data.
# If you don’t flush the compressor, you may not get any compressed output at all.

# You can also use a B
