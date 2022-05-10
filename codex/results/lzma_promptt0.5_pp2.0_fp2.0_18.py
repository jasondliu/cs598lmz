import lzma
# Test LZMADecompressor

# Get the test data
with open("../testdata/alice29.txt", "rb") as f:
    data = f.read()

# Compress with file API
with lzma.open("../testdata/alice29.txt.xz", "rb") as f:
    compressed = f.read()

# Decompress with LZMADecompressor
decomp = lzma.LZMADecompressor()
result = decomp.decompress(compressed)

print("Input length:", len(data))
print("Output length:", len(result))

if data == result:
    print("Everything OK")
else:
    print("Decompression failed")

# Test that the decompressor can be reused
data2 = decomp.decompress(b"garbage")
if data2 == b"":
    print("Decompressor can be reused")
else:
    print("Decompressor cannot be reused")

# Test that the decompressor can be copied
decomp2 = copy.copy(decomp)
if decomp2.
