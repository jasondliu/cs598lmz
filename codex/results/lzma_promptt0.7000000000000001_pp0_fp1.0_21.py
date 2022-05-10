import lzma
# Test LZMADecompressor
decompressor = lzma.LZMADecompressor()
decompressor.decompress('hello world')

with lzma.open(lzma_path) as f:
    file_content = f.read()
    decompressor.decompress(file_content)

import zlib
# Test ZlibCompressor
compressor = zlib.compressobj()
compressor.compress('hello world')

with open(zlib_path) as f:
    file_content = f.read()
    compressor.compress(file_content)


# Test ZlibDecompressor
decompressor = zlib.decompressobj()
decompressor.decompress('hello world')

with open(zlib_path) as f:
    file_content = f.read()
    decompressor.decompress(file_content)
