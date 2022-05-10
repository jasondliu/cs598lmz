import bz2
# Test BZ2Decompressor

comp_data = bz2.compress(b'This is a test')
comp_data

decomp = bz2.BZ2Decompressor()
decomp.decompress(comp_data)

