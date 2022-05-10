from bz2 import BZ2Decompressor
BZ2Decompressor().decompress('BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084')
# '*' is the decode from bz2 and '\x00' is the decode from hex

# From hex to decode '*' and '\x00'
BZ2Decompressor().decompress(codecs.decode(codecs.encode('*\x00', 'hex'), 'hex'))
# "congrats"

# To verify
BZ2Decompressor().decompress(b'BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x
