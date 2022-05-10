import lzma
# Test LZMADecompressor instances
raw1 = lzma.compress(b'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa')
raw2 = lzma.compress(b'bbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb')
raw3 = lzma.compress(b'cccccccccccccccccccccccccccccccc')
cmpr1 = (b'\xfd7zXZ' + raw1[:5])
cmpr2 = raw2[5:]
cmpr3 = raw3[10:]

decompressor = lzma.LZMADecompressor()

decompressor.decompress(cmpr1 + cmpr2)
decompressor.decompress(cmpr3)

decompressor.decompress(cmpr1 + cmpr3)
decompressor.decompress(cmpr2)

decompressor.decompress(cmpr1)
decompressor.decompress(cmpr2 + cmpr3)

assert decompressor.unused_data == b''

decompressor.
