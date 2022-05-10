import bz2
# Test BZ2Decompressor
bz2_decompressor = bz2.BZ2Decompressor()

result = bz2_decompressor.decompress(compressed_text)

print(result.decode())

print()

print(bz2_decompressor.decompress(compressed_text2))

print()

bz2_decompressor.decompress(compressed_text2)

print(bz2_decompressor.decompress(compressed_text3))

print()

print(bz2_decompressor.decompress(compressed_text3))

print()

bz2_decompressor.decompress(compressed_text3)

print(bz2_decompressor.decompress(compressed_text4))
