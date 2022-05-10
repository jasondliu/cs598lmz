import bz2
# Test BZ2Decompressor.incrementaldecompress()

# Issue #2241: crash when calling BZ2Decompressor.decompress() before
# BZ2Decompressor.decompress()
bz2decomp = bz2.BZ2Decompressor()
#try:
#    bz2decomp.decompress(b"")
#except IOError:
#    pass

data = test_support.findfile("test1.bz2")
if not data:
    test_support.test_skip('Could not find test1.bz2')
with open(data, 'rb') as f:
    data = f.read()

# Test incremental decompression
buf = b''
decomp = bz2.BZ2Decompressor()
for i in range(0, len(data), 8):
    buf += decomp.decompress(data[i:i+8])
buf += decomp.decompress(b'BZh91AY&SY\xab\xcd\xef\x00')

# Test the rest of the incremental decompression
