import bz2
# Test BZ2Decompressor class - decompression of textlines
data = b'BZh9\xb9\xae\x81\x8a\x00\x00\x00\x01\x00\x06\x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
print('Input contains ', len(data), ' bytes of compressed data')

decompressor = bz2.BZ2Decompressor()

for block in [data[:4], data[4:8], data[8:12], data[12:16]]:
    print(block, end=' ')
    print(decompressor.decompress(block), end=' ')
    print()

print(decompressor.decompress(data[16:]))
print('Uncompressed:', decompressor.unused_data)

# Test BZ2Decompressor class - decompression in chunks, with the unused data
# supply to start decompression
data = bz2.compress(b'BZh91AY
