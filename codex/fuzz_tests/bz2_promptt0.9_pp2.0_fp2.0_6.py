import bz2
# Test BZ2Decompressor
input = b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084'
c = bz2.BZ2Decompressor()
print(c.decompress(input))
print(c.unused_data)

try:
    c.decompress(b'xyzzy')
except EOFError:
    logging.exception('Expected exception')
else:
    assert 0, 'EOFError expected'

print(c.decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08'))
print(c.flush())

