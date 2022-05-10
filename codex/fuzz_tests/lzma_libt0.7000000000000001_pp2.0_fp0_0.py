import lzma
lzma.LZMADecompressor().decompress(open(sys.argv[0],"rb").read())
