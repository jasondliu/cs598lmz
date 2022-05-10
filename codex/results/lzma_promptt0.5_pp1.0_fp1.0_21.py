import lzma
# Test LZMADecompressor

# Decompress
with lzma.open('data/lzma_compressed.txt.xz') as f:
    file_content = f.read()

print(file_content)

# Compress
with lzma.open('data/lzma_compressed.txt.xz', 'w') as f:
    f.write(file_content)

with lzma.open('data/lzma_compressed.txt.xz') as f:
    file_content = f.read()

print(file_content)

# Compress
with lzma.open('data/lzma_compressed.txt.xz', 'w') as f:
    f.write(file_content)

with lzma.open('data/lzma_compressed.txt.xz') as f:
    file_content = f.read()

print(file_content)

# Decompress
with lzma.open('data/lzma_compressed.txt.xz') as f:
   
