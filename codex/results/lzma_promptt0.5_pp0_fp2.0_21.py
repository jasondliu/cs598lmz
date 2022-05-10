import lzma
# Test LZMADecompressor

decompressor = lzma.LZMADecompressor()

with lzma.open('input.xz') as f:
    while True:
        buf = f.read(65536)
        if not buf:
            break
        uncompressed = decompressor.decompress(buf)
        print(uncompressed)

decompressor.decompress(b'', True)
decompressor.decompress(b'', True)

# Test LZMADecompressor with multiple streams

decompressor = lzma.LZMADecompressor()

with lzma.open('input.xz') as f:
    while True:
        buf = f.read(65536)
        if not buf:
            break
        uncompressed = decompressor.decompress(buf)
        if uncompressed:
            print(uncompressed)
        else:
            print('---')

decompressor.decompress(b'', True)
decompressor.decompress(b'', True)

# Test
