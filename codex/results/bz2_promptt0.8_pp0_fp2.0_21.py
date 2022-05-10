import bz2
# Test BZ2Decompressor
#
# The BZ2Decompressor class is a little different from the others
# because it doesn't have an interface that is amenable to testing
# by feeding in just zlib.compress()'d data. The bz2 compressor
# keeps track of some internal state across multiple calls to
# compress() and flush(), and the compressed data it produces
# depends on this state. To work around this, we have to feed in
# real, compressed bz2 data.
#
# If we had a bunch of real, compressed bz2 data lying around, this
# wouldn't be a problem. But we don't, so we create some. The
# compresslevel keyword argument is supported by the bz2 module
# starting with Python 3.3, so we have to conditionally do things a
# little differently depending on which version we're running.
#
# To generate the data, we use two compressors. The compressor
# whose compressed data we use to test the BZ2Decompressor class is
# given compresslevel=9. The other compressor, whose output we
# discard, is given compresslevel=1 or, in Python 3
