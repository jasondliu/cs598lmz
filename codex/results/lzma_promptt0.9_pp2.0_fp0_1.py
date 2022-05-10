import lzma
# Test LZMADecompressor for full file output
with open('./extracted/13167fed-7e99-4e28-875d-3e8223fbabc3.csv', 'rb') as stream:
    dec = lzma.LZMADecompressor()
    # todo: decompress one chunk at a time, adjust chunk size, finish with a chunk = -1
    output = dec.decompress(stream.read())
    print(output)
    chunk_size = len(output)

# todo: zlib gzip for verification
import zlib
incompressible = b'Switch to time-based release instead of event based'
compressed = zlib.compress(incompressible, 2)
decompressed = zlib.decompress(compressed)
print(compressed)
print(decompressed)
decompressor = zlib.decompressobj()
print(decompressor.decompress(compressed))
print(decompressor.flush())


# todo: implement a file
from base_compression_wrapper import BaseCompressionWrapper, Comp
