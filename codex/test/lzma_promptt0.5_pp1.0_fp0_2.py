import lzma
# Test LZMADecompressor

data = b'1234567890' * 10000

comp = lzma.LZMACompressor()
comp_data = comp.compress(data) + comp.flush()

decomp = lzma.LZMADecompressor()
decomp_data = decomp.decompress(comp_data)

assert decomp_data == data
# Test LZMADecompressor with multiple streams

data = b'1234567890' * 10000

comp = lzma.LZMACompressor()
comp_data = comp.compress(data) + comp.flush()
