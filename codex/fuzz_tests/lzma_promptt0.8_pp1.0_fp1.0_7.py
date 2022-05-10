import lzma
# Test LZMADecompressor()
com = lzma.LZMACompressor()
com.compress(b'ffff')
com.flush()

dec = lzma.LZMADecompressor()
dec.decompress(b'ffff')
dec.flush()

# Test LZMADecompressor.decompress() with different buffer size
dec = lzma.LZMADecompressor()
dec.decompress(b'\xf0\x0f', 0)
dec.decompress(b'\x0f', 2)
dec.decompress(b'\xf0', 7)
dec.flush()

# Test LZMACoder class
# XXX: Do we need to test LZMACoder? It is an implementation detail
# and we already test compress/decompress in another test file.

# Test LZMAFilter class
lzf = lzma.LZMAFilter()
lzf.get_dict_size()
lzf.get_filters()

lzf = lzma.LZMAFilter(preset
