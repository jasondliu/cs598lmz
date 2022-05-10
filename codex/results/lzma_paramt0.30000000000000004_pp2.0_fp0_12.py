from lzma import LZMADecompressor
LZMADecompressor().decompress(data)

# 如果要压缩的数据很大，可以使用一个块压缩的方式处理
compressor = LZMACompressor()
compressor.compress(b'Some data')
compressor.compress(b'Some more data')
compressor.flush()

decompressor = LZMADecompressor()
decompressor.decompress(compressor.compress(b'Some data'))
decompressor.decompress(compressor.compress(b'Some more data'))
decompressor.flush()

# 如果要压缩的数据很大，可以使用一个块压缩的方式处理
compressor = LZMACompressor()
compressor.compress(b'Some data')
compressor.compress(b'Some more data')

