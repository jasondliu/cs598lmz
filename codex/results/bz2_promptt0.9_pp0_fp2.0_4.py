import bz2
# Test BZ2Decompressor instance's state - issue 1567
cdata = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
dc = bz2.BZ2Decompressor()
for c in cdata:
    r = dc.decompress(bytes([c]))
assert r == b'hello'
assert dc.unused_data == b''
dc = bz2.BZ2Decompressor()
r = dc.decompress(cdata)
assert r == b'hello'
assert dc.unused_data == b''
# test bz2.decompress()
for c in cdata:
    r = bz2.decompress(bytes([c]))
assert r == b'hello'
r = bz2.decompress(cdata)
assert r == b'hello
