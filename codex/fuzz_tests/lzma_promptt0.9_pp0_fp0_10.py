import lzma
# Test LZMADecompressor by feeding it every possible byte
# in order to test the internal state machine.

f = lzma._format.LZMADecompressor()

for i in range(256):
    f.decompress(bytes([i]))
f.decompress(b"", True)
