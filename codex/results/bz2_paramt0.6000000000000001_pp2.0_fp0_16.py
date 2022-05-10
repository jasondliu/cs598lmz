from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(compressed_data)

#compress and decompress data
uncompressed_data = b'We are the knights who say Ni!'
compressor = BZ2Compressor()
compressor.compress(uncompressed_data)
compressor.flush()
compressed_data = compressor.compress(uncompressed_data)

decompressor = BZ2Decompressor()
decompressor.decompress(compressed_data)

#using lzma
import lzma
compressed = lzma.compress(uncompressed_data)
original = lzma.decompress(compressed)

#lzma can be used for compressing and decompressing streams of data
compressor = lzma.LZMACompressor()
compressor.compress(uncompressed_data)
compressor.flush()

decompressor = lzma.LZMADecompressor()
decompressor.decompress(compressed_data)

#zlib
import zlib
compressed = zlib.compress(uncomp
