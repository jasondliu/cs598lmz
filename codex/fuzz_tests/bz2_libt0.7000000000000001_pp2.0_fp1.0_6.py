import bz2
bz2_comp=bz2.BZ2Compressor()
compressed=bz2_comp.compress(data)

print(compressed)
bz2_comp.flush()
print(compressed)


print('\n')

bz2_decomp=bz2.BZ2Decompressor()
decompressed=bz2_decomp.decompress(compressed)
print(decompressed)
print(data)
