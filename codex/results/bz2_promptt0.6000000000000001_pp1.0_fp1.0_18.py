import bz2
# Test BZ2Decompressor.

# This is a little more complicated than it needs to be, because
# the .test() method doesn't work very well in the face of padding
# bytes after the compressed data.  The .test() method is supposed
# to return the uncompressed data, but if there's padding bytes
# after the compressed data, it returns the uncompressed data plus
# the padding bytes.  The .read() method does the right thing, so
# we have to use that instead.

# (The padding bytes are inserted by bz2file.write() because the
# data has to be in blocks of 1000000 bytes.  The padding bytes are
# discarded by bz2file.read(), but they're not discarded by
# BZ2Decompressor.test().)

# The test data consists of the string 'abcdefghijklmnopqrstuvwxyz'
# repeated 10 times.

data = 'abcdefghijklmnopqrstuvwxyz' * 10

compressor = bz2.BZ2Compressor()
compressed = compressor.compress(data)
compressed +=
