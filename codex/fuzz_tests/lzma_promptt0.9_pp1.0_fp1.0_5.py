import lzma
# Test LZMADecompressor class from lzma module.

data_ext = ".lzma"

compressor = lzma.LZMACompressor(
		format=lzma.FORMAT_UNKNOWN, check=0, preset=level)
compressed_data = b""
compressed_chunk_size = 0
for data in [b"1", b"23", b"456"]:
	compressed_data += compressor.compress(data)
	compressed_chunk_size += len(compressor.compress(b""))
compressed_data += compressor.flush()
compressed_chunk_size += len(compressor.flush())

decompressor = lzma.LZMADecompressor(
		format=lzma.FORMAT_AUTO, memlimit=memlimit, filters=None)
compressed_file = io.BytesIO(compressed_data)
decompressed_data = b""
while True:
	compressed_chunk = compressed_file.read(compressed_chunk_size)
	if not compressed_chunk:
