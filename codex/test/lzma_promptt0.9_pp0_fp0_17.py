import lzma
# Test LZMADecompressor instances
raw1 = lzma.compress(b'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
raw2 = lzma.compress(b'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
raw3 = lzma.compress(b'cccccccccccccccccccccccccccccccc')
cmpr1 = (b'\xfd7zXZ' + raw1[:5])
cmpr2 = raw2[5:]
cmpr3 = raw3[10:]

decompressor = lzma.LZMADecompressor()

