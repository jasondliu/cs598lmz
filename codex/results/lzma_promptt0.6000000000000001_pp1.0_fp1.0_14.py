import lzma
# Test LZMADecompressor

data = b"".join(b"".join(struct.pack("!i", i) for i in range(1000)))

# Compress data
cdata = lzma.compress(data)

# Uncompress data
udata = lzma.decompress(cdata)

print("Compressed length", len(cdata))
print("Decompressed length", len(udata))

# Test decompressor
decompressor = lzma.LZMADecompressor()

# Feed compressed data in chunks
for i in range(0, len(cdata), 100):
    udata = decompressor.decompress(cdata[i:i+100])
    print("Decompressed length", len(udata))

# Finish decompression
udata += decompressor.decompress(b"")
print("Decompressed length", len(udata))

# Test reset
decompressor.reset()

# Decompress remaining data
udata = decompressor.decompress(cdata)
print("Decompressed length", len(ud
