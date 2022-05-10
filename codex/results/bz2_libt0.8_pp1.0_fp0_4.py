import bz2
bz2.BZ2Compressor().compress(b'It was a dark and stormy day.')

bz2.BZ2Decompressor().decompress(b'BZh91AY&SY\x[email protected]\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

import bz2
comp = bz2.BZ2Compressor()
comp.compress(b'It was a dark and stormy day. ')
comp.compress(b'It was a dark and stormy day. ')
comp.compress(b'It was a dark and stormy day. ')
comp.flush()

data = bz2.compress(b'It was a dark and stormy day. ')
bz2.decompress(data)

bz2.decompress(data * 100)

bz2.decompress(data * 100)[:30]


