import lzma
lzmacomp = lzma.LZMACompressor(check=-1)
lzmacomp.compress("parrot".encode("ascii"))

# lzma.LZMADecompressor

