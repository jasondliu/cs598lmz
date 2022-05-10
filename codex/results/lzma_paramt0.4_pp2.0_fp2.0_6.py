from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# decompress
with open('compressed_file.xz', 'rb') as input, open('decompressed_file', 'wb') as output:
    decompressor = LZMADecompressor()
    for block in iter(lambda: input.read(64 * 1024), b''):
        output.write(decompressor.decompress(block))
    output.write(decompressor.flush())

# compress
with open('decompressed_file', 'rb') as input, open('compressed_file.xz', 'wb') as output:
    compressor = LZMACompressor()
    for block in iter(lambda: input.read(64 * 1024), b''):
        output.write(compressor.compress(block))
    output.write(compressor.flush())
