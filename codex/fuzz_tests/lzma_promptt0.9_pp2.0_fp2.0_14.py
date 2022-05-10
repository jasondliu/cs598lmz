import lzma
# Test LZMADecompressor with a generator

def dec(data):
    decompressor = lzma.LZMADecompressor(dictionary=10)
    for block in data:
        yield decompressor.decompress(block)

data = [b"foo", b"barbaz", b"quuxbang", b"hooray", b"bingo"]

for i in dec(data):
    print(i)

print(dec(data))

for _, res in zip(data, dec(data)):
    print(res)

print(list(dec(data)))
# Test LZMADecompressor when reaching EOF

def dec(data):
    decompressor = lzma.LZMADecompressor(dictionary=10)
    for block in data:
        print(decompressor.decompress(block))

data = [b"foo", b"barbaz", b"quuxbang", b"hooray", b"bingo"]
dec(data)
# Test that LZMADecompressor works with zero-length blocks
