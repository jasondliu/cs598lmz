from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

# bz2
# bz2
import bz2
uncompressed_data = b'The same line, over and over.\n' * 1024
compressed_data = bz2.compress(uncompressed_data)
len(uncompressed_data)
len(compressed_data)

decompressor = bz2.BZ2Decompressor()
original_data = decompressor.decompress(compressed_data)
len(original_data)

original_data == uncompressed_data

compressor = bz2.BZ2Compressor()
compressor.compress(uncompressed_data)
compressor.flush()
data = compressor.compress(uncompressed_data) + compressor.flush()

decompressor.decompress(data)

data = bz2.compress(uncompressed_data) + b'\x00\x00\x00\x00'
decompressor.decompress(data)


# os.path模块
