import bz2
# Test BZ2Decompressor with a stream containing only the bzip2 end-of-stream (EOS) marker.
# This previously generated an error similar to "Unable to decompress data; code -1 = \
# BZ_UNEXPECTED_EOS".
t = bz2.BZ2Decompressor()
