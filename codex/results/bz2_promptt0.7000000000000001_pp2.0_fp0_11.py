import bz2
# Test BZ2Decompressor's readline()

decompressor = bz2.BZ2Decompressor()

compressed = bz2.compress(b"this is a test\n" * 10)
data = decompressor.decompress(compressed)

decompressor = bz2.BZ2Decompressor()

f = io.BytesIO(compressed)
line = decompressor.readline(f)
while line:
    print(line)
    line = decompressor.readline(f)

# Now, try the same thing with incremental decompression.

decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed[:5])
line = decompressor.unused_data
while line:
    print(line)
    decompressor.decompress(compressed[5:])
    line = decompressor.unused_data

print(decompressor.decompress(compressed[5:]))
