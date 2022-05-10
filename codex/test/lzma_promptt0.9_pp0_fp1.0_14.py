import lzma
# Test LZMADecompressor with LZMA-compressed data
# from Python 3.3's test_zlib
#
# To regenerate this test data, run:
#     data = b" ".join(str(i).encode() for i in range(1000))
#     encoded = lzma.compress(data, format=lzma.FORMAT_ALONE)
#     open("encoded.bin", "wb").write(encoded)
