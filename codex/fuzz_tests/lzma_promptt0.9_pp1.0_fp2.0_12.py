import lzma
# Test LZMADecompressor
def lzma2_test():
	d = lzma.LZMADecompressor()
	raw_data = b"this is uncompressed data"
	compressed_data = d.compress(raw_data)
	print compressed_data
	text_data = d.decompress(compressed_data)
	print text_data

# Compress Function
def compress_data_lzma(data):
	d = lzma.LZMADecompressor()
	compressed_data = d.compress(data)
	return compressed_data

# Decompress Function
def decompress_data_lzma(compressed_data):
	d = lzma.LZMADecompressor()
	text_data = d.decompress(compressed_data)
	return text_data


'''
Run this for the test
'''
def test():
	b = b"0123456789"
	s = compress_data_lzma(b)
	print (s)
	d = decompress_
