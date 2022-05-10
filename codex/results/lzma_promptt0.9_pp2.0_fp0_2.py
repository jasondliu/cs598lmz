import lzma
# Test LZMADecompressor
lz = lzma.LZMADecompressor()

decompressed = lz.decompress(compressed)

# .decompress() can be used multiple times
# as long as there's more data available.
more_data = lz.decompress(compressed)

lz = lzma.LZMADecompressor()
decompressed = lz.decompress(compressed)
 
# decompressed == more_data
type(decompressed)
decompressed
decompressed.decode("utf-8")
 
decompressed_custom = lz.decompress(compressed, 4)
more_data_custom = lz.decompress(compressed, 4)
# make_compressor() + make_decompressor()
lzdec = lzma.LZMADecompressor()
lzenc = lzma.LZMACompressor()
lzdec.decompress(lzenc.compress(b'add some data'))
lzdec.decompress(lzen
