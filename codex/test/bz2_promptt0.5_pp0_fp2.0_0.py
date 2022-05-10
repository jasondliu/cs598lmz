import bz2
# Test BZ2Decompressor.__init__()

# Check that the decompressor is initialised correctly

# Note that the decompressor is initialised to the state that it
# would be in if it had decompressed a stream consisting of only
# the start of a bzip2 stream, that is, it has no stored block
# metadata.

# Check that the decompressor is initialised correctly
decompressor = bz2.BZ2Decompressor()

# Check that the decompressor has no stored block metadata
