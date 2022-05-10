import lzma
# Test LZMADecompressor.
decomp = lzma.LZMADecompressor()

# decompress data incrementally
chunks = []
while True:
    chunk = decomp.decompress(compressed)
    if chunk:
        chunks.append(chunk)
    else:
        break

data = b''.join(chunks)
print('The decompressed data is {} bytes long.'.format(len(data)))

# using the context manager
with lzma.open('lorem.xz') as f:
    file_content = f.read()

print(file_content)

# Compressing with LZMA
with lzma.open('lorem.xz', 'w') as f:
    f.write(b'LZMA compression is great')

# Compression levels
with lzma.open('lorem-1.xz', 'w', preset=0) as f:
    f.write(b'This is the first example')

with lzma.open('lorem-9.xz', 'w', preset=9) as f
