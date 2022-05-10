import lzma
lzma.LZMADecompressor()
 
compressed_data = lzma.compress(b'Supercompressed')
print(len(compressed_data))

compressed_data = lzma.compress(b'Supercompressed')
compressor = lzma.LZMACompressor()
compressor.compress(b'Some data')
compressor.compress(b'Some data')
compressor.compress(b'Some data')

compressed_data = compressor.flush()
print(len(compressed_data))
