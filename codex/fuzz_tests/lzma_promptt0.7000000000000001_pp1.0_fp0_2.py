import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
compressed_data = open(lzma_file, 'rb').read()
original_data = decompressor.decompress(compressed_data)
open(uncomp_file, 'wb').write(original_data)
print(len(original_data), 'bytes of uncompressed data')

# Test LZMACompressor
compressor = lzma.LZMACompressor()
compressed_data = compressor.compress(original_data)
compressed_data += compressor.flush()
open(lzma_file, 'wb').write(compressed_data)
print(len(compressed_data), 'bytes of compressed data')

# Test LZMAFile
lz = lzma.LZMAFile(lzma_file, 'r')
output = lz.read()
print(len(output), 'bytes of uncompressed data read from LZMAFile')

# Test LZMAFile write
lz = lzma.LZMAFile(lzma_file, '
