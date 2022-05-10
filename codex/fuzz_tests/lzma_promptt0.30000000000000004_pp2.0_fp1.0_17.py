import lzma
# Test LZMADecompressor

# Compress a string
compressed = lzma.compress(b'Hello World!')

# Decompress a string
decompressed = lzma.decompress(compressed)

print(decompressed)

# Decompress a file
with lzma.open('lzma.txt.xz') as f:
    file_content = f.read()

print(file_content)

# Decompress a file with a custom filter
with lzma.open('lzma.txt.xz', format=lzma.FORMAT_XZ,
               filters=[{"id": lzma.FILTER_LZMA2, "preset": 3}]) as f:
    file_content = f.read()

print(file_content)

# Decompress a file with a custom filter and a custom memory limit
with lzma.open('lzma.txt.xz', format=lzma.FORMAT_XZ,
               filters=[{"id": lzma.FILTER_LZMA2, "
