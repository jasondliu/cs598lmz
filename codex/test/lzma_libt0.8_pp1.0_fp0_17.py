import lzma
lzma._decompressobj = lzma.LZMADecompressor
del lzma

