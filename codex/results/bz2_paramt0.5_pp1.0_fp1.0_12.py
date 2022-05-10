from bz2 import BZ2Decompressor
BZ2Decompressor()

# bz2.BZ2Decompressor.decompress(data)
# Decompress data, returning uncompressed data as bytes.

# bz2.BZ2Decompressor.flush()
# Flush the decompressor object and return any remaining data as bytes.

# bz2.BZ2Decompressor.copy()
# Return a copy of the decompressor object. This can be used to save the state of the decompressor so that it can be used to decompress data incrementally.

# bz2.BZ2Decompressor.eof
# True if the end-of-stream marker has been reached.

# bz2.BZ2Decompressor.unused_data
# The portion of the input data which was not used in the last decompress() operation.

# bz2.BZ2Decompressor.unconsumed_tail
# The portion of the input data which could not be decompressed because it was incomplete. This is always empty except when using an incremental decompressor.

# bz2.BZ2Decompressor.decompress(
