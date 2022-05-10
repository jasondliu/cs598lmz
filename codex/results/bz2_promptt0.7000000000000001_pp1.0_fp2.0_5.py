import bz2
# Test BZ2Decompressor
print(bz2.BZ2Decompressor().decompress(bz2_data))

# You can also construct a BZ2Decompressor object and repeatedly decompress data chunks
# with the decompress() method.
decompressor = bz2.BZ2Decompressor()
result = decompressor.decompress(bz2_data)
print(result)

# more_data = ...
result += decompressor.decompress(more_data)
print(result)

# While BZ2Decompressor objects can handle multiple compressed streams in a row,
# it’s not possible to use a single BZ2Compressor object to compress multiple data
# streams. You must create a new BZ2Compressor instance for each data stream.

# test bz2.open()
with bz2.open('compressedfile.bz2','wb') as output:
    output.write(b'Hello World')

with bz2.open('compressedfile.bz2','rb') as input:
    print(input.read(100))


