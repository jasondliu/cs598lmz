import lzma
# Test LZMADecompressor on a random byte sequence
import random
data = bytearray([random.randrange(256) for _ in range(4096)])
data = lzma.compress(data)
stream = lzma.LZMADecompressor()
decompressed = stream.decompress(data)
assert len(decompressed) == 4096
assert decompressed == bytes(bytearray([random.randrange(256) for _ in range(4096)]))
# We have one more byte than 4096 in the stream and have to
# call decompress() one more time before LZMADecompressor.eof
# becomes True. We
try:
    stream.decompress(b"")
except EOFError:
    pass
assert stream.eof
# The lifetime of a LZMADecompressor can be extended by reset().
previous_decompressed = decompressed
stream.reset()
decompressed = stream.decompress(data)
assert decompressed == previous_decompressed
# If a LZMADecompressor is created without a format flag, decomp
