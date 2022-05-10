import lzma
# Test LZMADecompressor
with open("data/Santorini.bin", "rb") as fin:
    data = fin.read()
lzma_dec = lzma.LZMADecompressor()
lzma_dec

lzma_dec = lzma.LZMADecompressor()
print(lzma_dec.decompress(data))
print(lzma_dec.unused_data)
print(lzma_dec.eof)
print(lzma_dec)
lzma_dec.decompress(data[:400])
print(lzma_dec.decompress(data[400:800]))
print(lzma_dec.decompress(data[800:]))
print(lzma_dec.unused_data)
print(lzma_dec.eof)

# Test LZMADecompressor decompress function
with open("data/Santorini.bin", "rb") as fin:
    data = fin.read()
with lzma.open("data/Santor
