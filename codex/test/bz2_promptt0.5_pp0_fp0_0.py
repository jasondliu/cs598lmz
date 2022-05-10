import bz2
# Test BZ2Decompressor.

# This is a guess at the minimum amount of data needed to trigger
# the bug.  If it's wrong, the test will fail with a short read
# exception.

# This test is skipped if the bz2 module wasn't compiled with the
# BZ2_DECOMPRESS_SMALL feature.

