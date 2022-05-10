import lzma
# Test LZMADecompressor 

lzdec = lzma.LZMADecompressor(format=lzma.FORMAT_RAW)
f = open("smallfile.xz", "rb")
lzdec.decompress(f.read())
f.close()

# Test XZUtils
with open("smallfile.xz", "rb") as f:
    xzutils.UnpackStream(f).read()
