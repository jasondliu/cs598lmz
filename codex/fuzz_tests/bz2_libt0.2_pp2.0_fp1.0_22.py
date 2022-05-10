import bz2
bz2.decompress(bz2_data)

# bz2.BZ2Decompressor()
# bz2_decompressor = bz2.BZ2Decompressor()
# bz2_decompressor.decompress(bz2_data)
# bz2_decompressor.flush()

# bz2.open()
with bz2.open('bz2_compressed.txt', 'rt') as input:
    print(input.read())

with bz2.open('bz2_compressed.txt', 'wt') as output:
    output.write('Contents go here.')

with bz2.open('bz2_compressed.txt', 'rt') as input:
    print(input.read())

# bz2.compress()
original_data = b'This is the original text.'
len(original_data)

compressed = bz2.compress(original_data)
len(compressed)

decompressed = bz2.decompress(compressed)

