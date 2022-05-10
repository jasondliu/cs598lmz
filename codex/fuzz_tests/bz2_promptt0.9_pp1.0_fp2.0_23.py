import bz2
# Test BZ2Decompressor
data = b'If compressed data is detected, autodetect its type and decompress it.'
compressor = bz2.BZ2Decompressor()
decomp = compressor.decompress(data)
print(decomp)

compressor = bz2.BZ2Compressor()
comp=  compressor.compress(decomp)
compressor.flush()
print(comp)

decompressor = bz2.BZ2Decompressor()
decompressed_data = decompressor.decompress(comp)
print(decompressed_data)
