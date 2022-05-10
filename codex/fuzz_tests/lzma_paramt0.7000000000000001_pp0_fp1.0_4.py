from lzma import LZMADecompressor
LZMADecompressorObj = LZMADecompressor()
data = LZMADecompressorObj.decompress(data)

print(data)

# Python3.3
import zlib
compressobj = zlib.compressobj(level=1)
compressed_data = compressobj.compress(data) + compressobj.flush()

decompressobj = zlib.decompressobj()
decompressed_data = decompressobj.decompress(compressed_data)

print(decompressed_data)
