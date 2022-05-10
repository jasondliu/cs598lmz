import lzma
lzma.LZMADecompressor(format=lzma.FORMAT_AUTO, memlimit=None, filters=None)

def unxz(src):
    with open(src, 'rb') as fd:
        decompressor = lzma.LZMADecompressor()
        return decompressor.decompress(fd.read())

