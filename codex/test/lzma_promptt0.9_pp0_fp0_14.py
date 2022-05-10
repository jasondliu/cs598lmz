import lzma
# Test LZMADecompressor on a random byte sequence
import random
data = bytearray([random.randrange(256) for _ in range(4096)])
data = lzma.compress(data)
stream = lzma.LZMADecompressor()
decompressed = stream.decompress(data)
assert len(decompressed) == 4096
