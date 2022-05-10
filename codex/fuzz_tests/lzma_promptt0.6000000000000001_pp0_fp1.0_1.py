import lzma
# Test LZMADecompressor
lzc = lzma.LZMACompressor()
lzc.compress(b"hello")
lzc.compress(b" ")
lzc.compress(b"world!")
lzc.flush()

lzd = lzma.LZMADecompressor()
# Feed the entire compressed data to the decompressor object.
data = lzc.flush()
print(lzd.decompress(data))

# Feed the compressed data to the decompressor in chunks.
offset = 0
chunk_size = 5
while True:
    chunk = data[offset:offset + chunk_size]
    if chunk:
        print(lzd.decompress(chunk))
        offset += len(chunk)
    else:
        break

# It is also possible to use the decompressor object as a context
# manager. This is useful for example if you want to decompress data
# that is stored in a file.
with lzma.LZMADecompressor() as lzd:
    with open("
