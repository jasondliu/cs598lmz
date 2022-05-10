import lzma
# Test LZMADecompressor.__init__()
comp = lzma.LZMADecompressor()
# Test LZMADecompressor.decompress()
comp = lzma.LZMADecompressor()
lzcomp = lzma.compress("1234567890")
pylzma_decomp = comp.decompress(lzcomp)
comp.decompress("1234")
comp.decompress("567890")
comp.decompress("1234567890")
# Test LZMADecompressor.decompress() via a buffer
comp = lzma.LZMADecompressor()
lzcomp = lzma.compress("1234567890")
buff = cStringIO.StringIO(lzcomp)
while True:
    data = buff.read(2)
    if not data:
        break
    got = comp.decompress(data)
    if got:
        print repr(got)
print repr(comp.unused_data)
# Test LZMADecompressor.flush()
sd
