import lzma
# Test LZMADecompressor.decompress()

with open('test.lzma', 'rb') as f:
    with lzma.LZMADecompressor() as dec:
        data = f.read()
        data1 = dec.decompress(data)
        data2 = dec.decompress(data)
        # data2 may be different from data1
