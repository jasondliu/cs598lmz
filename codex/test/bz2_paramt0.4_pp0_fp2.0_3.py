from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(b'BZh91AY&SY\x94$|\x0e\x00\x00\x00\x81\x00\x03$ \x00!\x9ah3M\x13<]\xc9\x14\xe1BBP\x91\xf08')

# bz2_decompress.py
from bz2 import BZ2Decompressor
decompressor = BZ2Decompressor()
with open('lorem.txt.bz2', 'rb') as input:
    with open('lorem.txt', 'wb') as output:
        while True:
            block = input.read(1024)
            if not block:
                break
            output.write(decompressor.decompress(block))
