from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(src_bz2)
bz2_data = src_bz2[:-4].decode('ascii')
print(bz2_data)

# .7z解凍
import lzma
with open(src_7z, 'rb') as f:
    raw = f.read()
cmpr = raw[:-5]
decmp = lzma.decompress(cmpr)
encmp = lzma.compress(decmp)
print(cmpr == encmp)
print(decmp.decode('ascii'))
print(''.join(chr(c) for c in decmp))
