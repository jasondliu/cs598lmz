import lzma
# Test LZMADecompressor is working

data = b"\xfd\x37\x7a\x58\x5a\x00\x00\x04\xe6\xd6\xb4\x46\x02\x00\x21\x01\x16\x00\xff\xff\xee\xee\xdd\xdd\x11\x22\x33\x44\x55\x66\x77\x88\x00"

with open("test.lzma", "wb") as f:
    f.write(data)

c = lzma.LZMADecompressor()
with open("test.lzma", "rb") as f:
    decompressed_data = c.decompress(f.read())

print(decompressed_data)

# '\xff\xff\xee\xee\xdd\xdd\x11\x22\x33\x44\x55\x66\x77\x88\x00'

# Note that this is the same as the data from the xz
