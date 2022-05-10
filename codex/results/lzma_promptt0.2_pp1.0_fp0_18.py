import lzma
# Test LZMADecompressor

with lzma.open('data/lzma_compressed.dat', mode='rb') as f:
    decompressor = lzma.LZMADecompressor()
    data = decompressor.decompress(f.read())
    print(data)

# Test LZMADecompressor.decompress()

with lzma.open('data/lzma_compressed.dat', mode='rb') as f:
    decompressor = lzma.LZMADecompressor()
    data = f.read()
    while True:
        chunk = decompressor.decompress(data)
        if chunk == b'':
            break
        print(chunk)
        data = decompressor.unconsumed_tail

# Test LZMADecompressor.decompress() with max_length

with lzma.open('data/lzma_compressed.dat', mode='rb') as f:
    decompressor = lzma.LZMADecompressor()
    data = f.read()
    while
