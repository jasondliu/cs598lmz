import lzma
# Test LZMADecompressor

compressed = lzma.compress(b'This is a test')
compressed

compressor = lzma.LZMACompressor()
compressor.compress(b'This is a test')
compressor.flush()
compressor.compress(b'This is a test')
compressor.flush()

decompressor = lzma.LZMADecompressor()
decompressor.decompress(compressed)

decompressor.decompress(compressor.compress(b'This is a test'))
decompressor.decompress(compressor.flush())

try:
    decompressor.decompress(b'garbage')
except lzma.LZMAError:
    print('LZMAError')
# Test LZMADecompressor with a file

with lzma.open('lzma_compressed.xz', 'wb') as f:
    f.write(b'This is the uncompressed data. ' * 10000)

with lzma.open('lzma_compressed.
