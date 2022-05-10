import bz2
# Test BZ2Decompressor

compressor = bz2.BZ2Compressor()
decompressor = bz2.BZ2Decompressor()

# compress some data
data = "This is a test of the BZ2Compressor and BZ2Decompressor classes."

