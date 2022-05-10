import lzma
# Test LZMADecompressor
from io import BytesIO
compressor = lzma.LZMACompressor()

compressed_data = compressor.compress(b"test")
compressed_data += compressor.flush()
print(compressed_data)

decompressor = lzma.LZMADecompressor()
print(decompressor.decompress(compressed_data))

data = BytesIO(compressed_data)
decompressor = lzma.LZMADecompressor()
print(decompressor.decompress(data.read()))
 
# Test LZMADecompressor
from io import BytesIO
compressor = lzma.LZMACompressor()

compressed_data = compressor.compress(b"test")
compressed_data += compressor.flush()
print(compressed_data)

decompressor = lzma.LZMADecompressor()
print(decompressor.decompress(compressed_data))

data = BytesIO(compressed_data)
decompressor = lz
