import lzma
# Test LZMADecompressor with a variety of different input sizes, including
# ones that are a multiple of the internal buffer size
for i in range(1, 33):
    data = b'x' * i
    comp = lzma.LZMACompressor()
    cdata = comp.compress(data)
    cdata += comp.flush()
    dec = lzma.LZMADecompressor()
    newdata = dec.decompress(cdata)
    if newdata == data:
        print(i)
    else:
        print(i, "ERROR")
# Test LZMADecompressor with previously compressed data
data = b'x' * 1000 + b'y' * 1000
comp = lzma.LZMACompressor()
cdata = comp.compress(data)
cdata += comp.flush()
dec = lzma.LZMADecompressor()
newdata = dec.decompress(cdata)
if newdata == data:
    print("OK 1")
else:
    print("ERROR 1")
newdata = dec.decompress
