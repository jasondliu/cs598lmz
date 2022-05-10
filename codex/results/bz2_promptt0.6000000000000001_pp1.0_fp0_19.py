import bz2
# Test BZ2Decompressor
source = bz2.BZ2File('example.txt.bz2')
dest = open('uncompressed.txt', 'wb')
decompressor = bz2.BZ2Decompressor()

while True:
    block = source.read(1024)
    if not block:
        break
    uncompressed = decompressor.decompress(block)
    if uncompressed:
        dest.write(uncompressed)
source.close()
dest.close()

# The bz2 module also supports incremental compression.
# You can compress data by feeding it in chunks to a BZ2Compressor object
# and retrieve the compressed data by calling its compress() or flush() method.
compressor = bz2.BZ2Compressor()
source = open('example.txt', 'rb')
while True:
    block = source.read(1024)
    if not block:
        break
    compressed = compressor.compress(block)
    if compressed:
        print(compressed)
remainder = compressor.flush()
print(remainder)

# The b
