import lzma
lzma.decompress(data)

# Compress data
data = b"Lots of content here"
compressed = lzma.compress(data)

# Round-trip the data
original = lzma.decompress(compressed)
original == data

# Compress an iterable
data = [b"Lots of", b"small chunks", b"of content"]
compressed = b"".join(lzma.compress(chunk) for chunk in data)

# Decompress an iterable
decompressor = lzma.LZMADecompressor()
decompressed_data = []
for chunk in [compressed]:
    decompressed_data.append(decompressor.decompress(chunk))
decompressed_data

# Compress with a preset
data = b"Lots of content here"
compressed = lzma.compress(data, preset=9 | lzma.PRESET_EXTREME)

# Decompress with a preset
data = b"Lots of content here"
compressed = lzma.
