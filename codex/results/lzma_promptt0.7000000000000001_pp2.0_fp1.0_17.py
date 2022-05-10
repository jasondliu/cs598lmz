import lzma
# Test LZMADecompressor

d = lzma.LZMADecompressor()
with open('data/lzma_data.xz', 'rb') as f:
    try:
        print(d.decompress(f.read()))
    except EOFError as e:
        print(e)

# Test LZMACompressor
# note: lzma.LZMACompressor.compress returns nothing

c = lzma.LZMACompressor()
with open('data/lzma_data.xz', 'wb') as f:
    try:
        f.write(c.compress(b"LZMA compression is cool"))
    except EOFError as e:
        print(e)
