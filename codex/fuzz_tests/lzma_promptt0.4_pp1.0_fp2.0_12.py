import lzma
# Test LZMADecompressor

# Create a LZMA-compressed string
comp = lzma.LZMACompressor()
data = comp.compress(b"Hello World")
data += comp.flush()

# Decompress it
decomp = lzma.LZMADecompressor()
print(decomp.decompress(data))

# Decompress it again
print(decomp.decompress(data))

# Decompress it again
print(decomp.decompress(data))

# Decompress it again
print(decomp.decompress(data))

# Decompress it again
print(decomp.decompress(data))

# Decompress it again
print(decomp.decompress(data))

# Decompress it again
print(decomp.decompress(data))

# Decompress it again
print(decomp.decompress(data))

# Decompress it again
print(decomp.decompress(data))

# Decompress it again
print(decomp.decomp
