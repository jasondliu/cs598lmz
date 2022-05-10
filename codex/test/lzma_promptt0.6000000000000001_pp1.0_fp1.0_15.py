import lzma
# Test LZMADecompressor's ability to handle data that's not encoded with
# LZMA_CONCATENATED.
for i in range(1, 8):
    data = b'\x00' * i
