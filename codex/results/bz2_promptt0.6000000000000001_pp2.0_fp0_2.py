import bz2
# Test BZ2Decompressor with multiple input streams.

test_string = b"Hello world!\n"
compressed_string = bz2.compress(test_string)
compressed_string += bz2.compress(b"This is a test\n")
compressed_string += bz2.compress(b"Goodbye, world!\n")

d = bz2.BZ2Decompressor()
try:
    print(d.decompress(compressed_string))
except EOFError:
    print("EOFError raised, as expected")

d = bz2.BZ2Decompressor()
print(d.decompress(compressed_string[:30]))
print(d.decompress(compressed_string[30:]))

d = bz2.BZ2Decompressor()
print(d.decompress(compressed_string[:30]), end="")
print(d.decompress(compressed_string[30:]), end="")

# Check that the BZ2Decompressor can be used as an iterator

