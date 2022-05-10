import lzma
# Test LZMADecompressor
#
# This test is intended to be run with a single command line argument, which
# should be the name of a file containing a single compressed stream.
#
# The test will read the file and decompress it using the LZMADecompressor
# class.  The decompressed data will be compared against the original data.
#
# The test will also decompress the input data in chunks of various sizes
# and compare the results.

# Read the entire input file
with open(sys.argv[1], 'rb') as f:
    data = f.read()

# Decompress the entire input file
d = lzma.LZMADecompressor()
decompressed = d.decompress(data)

# Verify that the decompressed data matches the original data
if decompressed != data:
    raise Exception(
        "Decompressed data does not match original data!")

# Decompress the input file in chunks of 1, 2, 3, ... bytes
for i in range(1, len(data)):
    d = lzma.LZMADecomp
