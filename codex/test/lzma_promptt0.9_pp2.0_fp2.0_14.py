import lzma
# Test LZMADecompressor with a generator

def dec(data):
    decompressor = lzma.LZMADecompressor(dictionary=10)
    for block in data:
        yield decompressor.decompress(block)

data = [b"foo", b"barbaz", b"quuxbang", b"hooray", b"bingo"]

