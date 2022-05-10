import lzma
# Test LZMADecompressor module
decomp = lzma.LZMADecompressor()
with open("data/pic.jpg", "rb") as fd:
    unzipped = decomp.decompress(fd.read())
    print(unzipped)
