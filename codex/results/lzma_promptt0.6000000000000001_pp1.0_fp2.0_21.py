import lzma
# Test LZMADecompressor
lzc = lzma.LZMADecompressor()
lzc.decompress(compressed)

# Test LZMAFile
with lzma.open("compressedfile", "wb") as f:
    f.write(compressed)
with lzma.open("compressedfile") as f:
    uncompressed2 = f.read()

print(uncompressed2 == uncompressed)

# Test LZMAError
try:
    lzc.decompress(b"garbage")
except lzma.LZMAError:
    print("caught as LZMAError")

# Test XZFile
with lzma.open("compressedfile", "w") as f:
    f.write(compressed)
with lzma.open("compressedfile") as f:
    uncompressed2 = f.read()

print(uncompressed2 == uncompressed)

# Test XZFile with preset
with lzma.open("compressedfile", "w", preset=9) as f:
    f.
