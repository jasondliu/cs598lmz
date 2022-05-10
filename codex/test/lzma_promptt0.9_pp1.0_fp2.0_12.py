import lzma
# Test LZMADecompressor
def lzma2_test():
	d = lzma.LZMADecompressor()
	raw_data = b"this is uncompressed data"
	compressed_data = d.compress(raw_data)
