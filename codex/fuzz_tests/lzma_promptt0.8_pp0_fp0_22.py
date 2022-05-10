import lzma
# Test LZMADecompressor()

cdata = lzma.compress(b"hello123world")
print("Compressed Data:", cdata)
d = lzma.LZMADecompressor()
data = d.decompress(cdata)
print("Decompressed Data:", data)
if d.unused_data != b"":
    print("Unused Data:", d.unused_data)
if bool(d.eof):
    print("End of Stream")
del d

d = lzma.LZMADecompressor()
for i in cdata:
    data = d.decompress(bytes([i]))
    print("Decompressed Data:", data)
if d.unused_data != b"":
    print("Unused Data:", d.unused_data)
if bool(d.eof):
    print("End of Stream")
del d

print("Stream compression")
with lzma.open("test.xz", "w") as f:
    f.write("hello123world")

with lzma
