import bz2
# Test BZ2Decompressor with a stream that has multiple concatenated bz2 streams

TEST_FILE = "test/data/sample1.bz2"

# Read the whole file, decompress it, and check that the result is as expected.
