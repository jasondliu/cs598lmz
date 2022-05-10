import bz2
# Test BZ2Decompressor
bz2_decomp = bz2.BZ2Decompressor()
bz2_decomp.decompress(bz2_data)

# Test BZ2Compressor
bz2_comp = bz2.BZ2Compressor()
bz2_comp.compress(bz2_data)
bz2_comp.flush()

# Test BZ2File
bz2.BZ2File(bz2_data)

# Test IncrementalDecoder
bz2_decomp = bz2.IncrementalDecompressor()
bz2_decomp.decompress(bz2_data)
