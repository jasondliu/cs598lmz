import bz2
# Test BZ2Decompressor().decompress()

# Issue 17667: BZ2Decompressor().decompress() could get stuck on incomplete
# data.

data = 'BZh91AY&SY.\xc8N\x18\x00\x01>_\x80\x00\x10@\x02\xff\xf0\x01\x07n\x00?'
decomp = bz2.BZ2Decompressor()
try:
    decomp.decompress(b'xx')
except IOError as msg:
    assert msg.args == ('Invalid data stream',)
else:
    print('Expected an exception')

partial = decomp.decompress(data[:10])
assert not partial

partial = decomp.decompress(data[10:20])
assert not partial

partial = decomp.decompress(data[20:])
assert partial == b'hello'

partial = decomp.decompress(data[20:])
assert not partial

# Test BZ2Decompressor().decompress().__self__ for cyclic garbage collection

