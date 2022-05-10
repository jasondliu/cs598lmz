from lzma import LZMADecompressor
LZMADecompressor(format=FORMAT_AUTO, memlimit=None, filters=None)

with open(filename, 'rb') as fh:
    #data = fh.read()
    a = fh.read(10)
    #b = fh.read(10)
    #c = fh.read(10)
    #d = fh.read(10)

decompressor = LZMADecompressor()
decompressor.decompress(a)
decompressor.decompress(b)
decompressor.decompress(c)
decompressor.decompress(d)
</code>

