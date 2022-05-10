import bz2
# Test BZ2Decompressor.__init__()
try:
    bz2.BZ2Decompressor()
except:
    print('SKIP')
    raise SystemExit

# Test BZ2Decompressor.__init__(wbits)
try:
    bz2.BZ2Decompressor(bz2.BZ2_DECOMPRESSION_SMALL)
    bz2.BZ2Decompressor(9)
except:
    print('SKIP')
    raise SystemExit

# Test BZ2Decompressor.decompress(data)
d = bz2.BZ2Decompressor()
d.decompress(b'BZh91AY&SY')
try:
    d.decompress(b'x')
    print('SKIP')
    raise SystemExit
except EOFError:
    print('EOFError')

# Test BZ2Decompressor.unused_data
d = bz2.BZ2Decompressor()
print(d.unused_data)
