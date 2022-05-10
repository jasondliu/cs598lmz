import bz2
# Test BZ2Decompressor.decompress() with a large input.

decompressor = bz2.BZ2Decompressor()

# The input is a repetition of the string 'a' * 100.
input = ('a' * 100 + '\n') * 100000

# The output is a repetition of the string 'a' * 1000000.
output = ('a' * 1000000 + '\n') * 10

# Decompress the input.
result = decompressor.decompress(input)

# Check that the result is correct.
if result != output:
    raise RuntimeError("decompressor.decompress() returned %d bytes, "
                       "expected %d" % (len(result), len(output)))

# Check that the decompressor is exhausted.
if decompressor.unused_data != "":
    raise RuntimeError("decompressor.unused_data is not empty")
