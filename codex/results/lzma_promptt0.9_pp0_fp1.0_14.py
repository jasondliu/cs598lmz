import lzma
# Test LZMADecompressor with LZMA-compressed data
# from Python 3.3's test_zlib
#
# To regenerate this test data, run:
#     data = b" ".join(str(i).encode() for i in range(1000))
#     encoded = lzma.compress(data, format=lzma.FORMAT_ALONE)
#     open("encoded.bin", "wb").write(encoded)
encoded = open("encoded.bin", "rb").read()

decomp = lzma.LZMADecompressor()

if decomp.eof:
    raise Exception("Wrong eof state at init")

piece1 = encoded[:16]
piece2 = encoded[16:-1]
piece3 = encoded[-1:]

if decomp.eof:
    raise Exception("Wrong eof state")

chunk1 = decomp.decompress(piece1)

if len(chunk1) != 0:
    raise Exception("Incorrect amount of data returned "
            "(expected 0, got %d)" % len(chunk
