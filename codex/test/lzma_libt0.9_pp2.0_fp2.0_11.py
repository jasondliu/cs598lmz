import lzma
lzma_compress = lzma.compress
lzma_decompress = lzma.decompress
lzma_compressLevel = lzma.PRESET_EXTREME
if hasattr(lzma, "LZMA_VERSION_NUMBER"):
	lzma_version = lzma.LZMA_VERSION_NUMBER
else:
	lzma_version = 2

