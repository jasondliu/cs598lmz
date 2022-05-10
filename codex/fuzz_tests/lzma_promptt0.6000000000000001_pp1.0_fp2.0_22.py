import lzma
# Test LZMADecompressor
data = b"".join(open("testdata/alice29.txt", "rb").readlines())
cdata = lzma.compress(data)
d = lzma.LZMADecompressor()
print(d.decompress(cdata))
print(d.unconsumed_tail)
print(d.eof)

# Test LZMAFile
f = lzma.open("testdata/alice29.txt.xz", "r")
print(f.read())
print(f.read())

# Test LZMAFile with non-seekable stream
import io
s = io.BytesIO(lzma.compress(b"test"))
f = lzma.open(s, "r")
print(f.read())
print(f.read())

# Test LZMAFile with seekable stream
s = io.BytesIO(lzma.compress(b"test"))
f = lzma.open(io.BufferedReader(s), "r")
print(f.read())
print(f
