import lzma
lzma.compress
try:
	LZMACompressor = lzma.LZMACompressor
except AttributeError:
	LZMACompressor = lzma.compress


