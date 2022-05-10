import lzma
# Test LZMADecompressor.

print("Testing LZMADecompressor")

with open("testdata/alice29.txt", "rb") as f:
    data = f.read()

with open("testdata/alice29.txt.lzma", "rb") as f:
    compressed = f.read()

d = lzma.LZMADecompressor()
decompressed = d.decompress(compressed)

if data == decompressed:
    print("OK")
    exit(0)
else:
    print("ERROR")
    exit(1)
