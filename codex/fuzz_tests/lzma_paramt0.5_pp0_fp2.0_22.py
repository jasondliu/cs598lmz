from lzma import LZMADecompressor
LZMADecompressor().decompress(compressed_data)

# %%
# Compressing data in memory with context managers

# Compress a file
with lzma.open('compressed_file.xz', 'wt') as f:
    f.write(data)

# Decompress
with lzma.open('compressed_file.xz', 'rt') as f:
    text = f.read()

# %%
# Compressing and decompressing using streams

# Compress
with lzma.open('compressed_file.xz', 'w') as f:
    with open('original_file', 'rb') as input:
        f.write(input.read())

# Decompress
with lzma.open('compressed_file.xz', 'r') as f:
    with open('uncompressed_file', 'wb') as output:
        output.write(f.read())

# %%
# Decompressing with a preset

# Compress
with lzma.open('compressed_file.xz', 'w', preset=9
