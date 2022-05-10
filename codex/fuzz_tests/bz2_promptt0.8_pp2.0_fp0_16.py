import bz2
# Test BZ2Decompressor class
with open('compresstest') as fo:
    data = fo.read()

compressor = bz2.BZ2Compressor()
for line in data.splitlines():
    compressed_line = compressor.compress(line.encode())

with open('compressed', 'wb') as fo:
    fo.write(compressor.flush())

decompressor = bz2.BZ2Decompressor()
with open('compressed') as fo:
    data = fo.read()
    decompressed_data = decompressor.decompress(data)

lines = decompressed_data.decode().splitlines()
assert lines[0] == 'A very "compressed" file, I hope...'
assert len(lines) == 11
import bz2
# Working with files - part II
with bz2.BZ2File('compressed', 'rb') as fo:
    data = fo.read()

decompressor = bz2.BZ2Decompressor()
decompressed_data = decompressor.decompress(data)
lines
