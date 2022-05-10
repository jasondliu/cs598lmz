import lzma
# Test LZMADecompressor

# Test LZMADecompressor.decompress()
# Test LZMADecompressor.decompress(max_length)
# Test LZMADecompressor.decompress(max_length) with max_length < 0
# Test LZMADecompressor.decompress(max_length) with max_length == 0
# Test LZMADecompressor.decompress(max_length) with max_length > 0
# Test LZMADecompressor.decompress(max_length) with max_length > 0 and max_length < len(data)
# Test LZMADecompressor.decompress(max_length) with max_length > 0 and max_length == len(data)
# Test LZMADecompressor.decompress(max_length) with max_length > 0 and max_length > len(data)
# Test LZMADecompressor.decompress(max_length) with max_length > 0 and max_length > len(data) and max_length < len(data) +
