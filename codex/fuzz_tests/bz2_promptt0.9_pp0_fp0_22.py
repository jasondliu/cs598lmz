import bz2
# Test BZ2Decompressor
test_str = 'hello world'
# Encode the string
coded = bz2.compress(test_str)
print coded

# Decode the string
print bz2.decompress(coded)

# Only decode the first
print bz2.decompress(coded, 1)

# Prints the raw compressed data out
print coded[1]

# Creates a decompressor object
decompressor = bz2.BZ2Decompressor()
# Allow it to process the data as a file
print decompressor.decompress(coded)

# Null BZ2Decompressor
decompressor = bz2.BZ2Decompressor()

# Feeds the decompressor the raw compressed data
print decompressor.decompress(coded[1])

# Decompresses more of the data
print decompressor.decompress(coded[2:])

# Need to handle the trailing data differently
print decompressor.decompress(coded[-1])

# Test BZ2Compressor

# Creates a compressor object
compressor = b
