import lzma
# Test LZMADecompressor.decompress()

# The LZMA format has a special header that is not part of the compressed data
# stream.  This header is used to initialize the LZMA decoder.  The header is
# not included in the compressed data stream.  The compressed data stream
# consists of a series of chunks.  Each chunk has a 5-byte header followed by
# the compressed data.  The header is a little-endian encoded 32-bit integer
# that is the length of the uncompressed data for that chunk.  The compressed
# data for the chunk is encoded in the LZMA format.  The compressed data
# stream is terminated by a chunk with a length of 0.

# This function tests the LZMA decoder by feeding it a series of chunks.  The
# chunks are constructed by taking the uncompressed data and compressing it
# using the LZMA format.  The LZMA format has a special header that is not
# part of the compressed data stream.  This header is used to initialize the
# LZMA decoder.  The header is not included in the compressed data stream.
# The compressed data stream consists
