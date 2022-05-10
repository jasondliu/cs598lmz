import lzma
# Test LZMADecompressor.
decompressor = lzma.LZMADecompressor()
data = b'\x00\x00\x00\x00\x00\x00\x00\x00W\x13\x00\x00\x00\x00\x00\x00\x00'
decompressor.decompress(data)
decompressor.flush()

# Test LZMACompressor.
compressor = lzma.LZMACompressor()
compressor.compress(b"Test")
compressor.flush()

# Test LZMAFile

with open('lzma.py', 'rb') as fileobj:
    with lzma.open(fileobj, mode='rb') as f:
        for line in f:
            print(line)
