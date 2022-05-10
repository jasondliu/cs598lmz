from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# bz2.open()
with bz2.open('file.bz2', 'rt') as f:
    data = f.read()

# bz2.compress()
data = b'Lots of data...'
len(data)

compressed = bz2.compress(data)
len(compressed)

# bz2.decompress()
decompressed = bz2.decompress(compressed)
len(decompressed)

# bz2.BZ2Compressor()
compressor = bz2.BZ2Compressor()
compressor.compress(data)
compressor.flush()

# bz2.BZ2Decompressor()
decompressor = bz2.BZ2Decompressor()
decompressor.decompress(compressed)

# bz2.open()
with bz2.open('file.bz2', 'wt') as f:
    f.write(data)

with bz2.open
