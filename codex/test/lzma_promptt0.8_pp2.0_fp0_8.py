import lzma
# Test LZMADecompressor
data = b'\x00\x04\xe6\xd6\xb4\x46\x02\x00\x21\x01\x1c\x00\x00\x00'
c = lzma.LZMADecompressor()

try:
    print(c.decompress(data))
except lzma.LZMAError:
    print("Error:")
    print([hex(x) for x in data])


# Codec APIs
import lzma
import binascii

