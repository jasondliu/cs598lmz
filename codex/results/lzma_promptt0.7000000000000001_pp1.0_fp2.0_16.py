import lzma
# Test LZMADecompressor()

##  Input data
cdata = lzma.compress(b"Hello World!")

##  Decompressor object
d = lzma.LZMADecompressor()

##  Decompressed data
ddata = d.decompress(cdata)

##  Decompressed data is the same as original data
if ddata == b"Hello World!":
    print("Success")

print(len(cdata))
print(len(ddata))

##  Decompressor object can be used repeatedly
d = lzma.LZMADecompressor()
d.decompress(b'\x00\x00\x80\x00\xfb\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\
