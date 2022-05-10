import lzma
# Test LZMADecompressor
decomp = lzma.LZMADecompressor()
#with open('data/compressed_lzma.txt', 'rb') as comp_file:
with open('data/compressed_lzma.txt', 'rb') as comp_file:
    comp_data = comp_file.read()
    decomp_data = decomp.decompress(comp_data)
print(decomp_data)

# Test LZMACompressor
#comp = lzma.LZMACompressor()
#comp_data = comp.compress(b'data to compress')
#comp_data += comp.flush()
#print(comp_data)

# lzma.open()
#with lzma.open('data/compressed_lzma.txt', 'rb') as comp_file:
#    comp_data = comp_file.read()
#    print(comp_data)
