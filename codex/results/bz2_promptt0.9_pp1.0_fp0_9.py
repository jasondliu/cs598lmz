import bz2
# Test BZ2Decompressor functions in module
dec = bz2._BZ2Decompressor()
data = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
after = dec.decompress(data)
test_expectation(len(after) == 24, 'initialize decompressor')
test_expectation(dec.decompress(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00') == b'', 'compressed data with zero as last byte')

after = after + dec.decompress(b'1\xc0\x00\xff\xff')
test_expectation(len(after) == 41, 'additional decompress')
after = after + dec.decompress(dec.flush())
test_expectation
