import bz2
# Test BZ2Decompressor -- a lot of data to decompress, and some random
# seeks, but the data is short enough that we can just save it in memory
# and compare it to the reference output
decomp = bz2.BZ2Decompressor()
compr = bz2.compress(open(bz2.__file__, 'rb').read())
decompdata = decomp.decompress(compr)
assert decompdata == open(bz2.__file__, 'rb').read()
assert decomp.decompress(b'') == b''
assert decomp.decompress(b'\x42\x5a\x68') == b''
assert decomp.unconsumed_tail == decomp.decompress(b'\x42\x5a\x68') == b''
decomp.decompress(b'\x42\x5a')
assert decomp.decompress(b'\x68') == b'h'
assert decomp.unconsumed_tail == b''
datalen = len(decompdata)
for i in range(100):
    r
