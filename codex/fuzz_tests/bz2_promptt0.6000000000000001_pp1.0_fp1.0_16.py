import bz2
# Test BZ2Decompressor by decompressing a file.

decomp = bz2.BZ2Decompressor()

original_data = open('lorem.txt', 'rb').read()
compressed = bz2.compress(original_data)

# Feed the compressed data in 8192 byte chunks.
decompressed = decomp.decompress(compressed)

# Check that the decompressed data is the same as the original.
if decompressed == original_data:
    print("It works!")
else:
    print("Something went wrong!")

# Feed in some more data, just to make sure it doesn't have any issues.
try:
    decomp.decompress(b'\x00\x00\x00\x00\x00')
except EOFError:
    print("EOFError: that is all the data")
else:
    print("Something went wrong!")


# Test BZ2Decompressor by decompressing a file and writing to a file-like object.

decomp = bz2.BZ2Decompressor()

original_data = open('
