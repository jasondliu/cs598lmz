import lzma
# Test LZMADecompressor object

from io import TextIOWrapper

compressor = lzma.LZMACompressor()

text = "Test string 1\nTest string 2".encode('utf-8')
compressed = compressor.compress(text)

print("Compressed: ", compressed)

decompressor = lzma.LZMADecompressor()
output_buffer = decompressor.decompress(compressed)
print("Decompressed:", output_buffer.decode('utf-8'))

