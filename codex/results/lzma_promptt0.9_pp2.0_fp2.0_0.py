import lzma
# Test LZMADecompressor module
cd = lzma.LZMADecompressor()
print("In: {}".format(cd.getbuffer()))
out = cd.decompress(b"P^\xcf\xc9d\x00\x00\x00\x00\x00\x18\x00\x036\x00\x00\x00\x0b")
print("Out: {}".format(out))
