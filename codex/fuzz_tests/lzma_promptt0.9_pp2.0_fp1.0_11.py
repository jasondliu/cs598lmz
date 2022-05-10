import lzma
# Test LZMADecompressor
def test():
    cmp = lzma.LZMADecompressor()
    f = open("___", "rb")
    buf = f.read()
    f.close()
    ret = cmp.decompress(buf)
    f = open("___", "wb")
    buf = f.write(ret)
    f.close()
