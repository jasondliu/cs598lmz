import lzma
# Test LZMADecompressor.

decompressor = lzma.LZMADecompressor()

# Decompress the data.
with open("test.xz", "rb") as f:
    data = decompressor.decompress(f.read())

# Check if the decompression was successful.
if data:
    print("Decompression was successful.")
else:
    print("Decompression failed.")

# Decompress the data.
with open("test.xz", "rb") as f:
    data = decompressor.decompress(f.read())

# Check if the decompression was successful.
if data:
    print("Decompression was successful.")
else:
    print("Decompression failed.")
