import lzma
# Test LZMADecompressor

comp = lzma.LZMACompressor()
data = b'this is the data to compress'
compressed = comp.compress(data)
compressed += comp.flush()

decomp = lzma.LZMADecompressor()
decompressed = decomp.decompress(compressed)
decompressed == data

# Test LZMADecompressor.decompress()

decomp = lzma.LZMADecompressor()
decompressed = decomp.decompress(compressed)
decompressed == data
decomp.decompress(b'')
decomp.decompress(b'garbage')

# Test LZMADecompressor.decompressobj()

decomp = lzma.LZMADecompressor()
decompressobj = decomp.decompressobj()
decompressed = decompressobj.decompress(compressed)
decompressed == data

decompressobj = lzma.LZMADecompressor().decompressobj()
decompressed
