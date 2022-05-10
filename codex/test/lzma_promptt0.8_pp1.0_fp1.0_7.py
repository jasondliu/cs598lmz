import lzma
# Test LZMADecompressor()
com = lzma.LZMACompressor()
com.compress(b'ffff')
com.flush()

dec = lzma.LZMADecompressor()
dec.decompress(b'ffff')
