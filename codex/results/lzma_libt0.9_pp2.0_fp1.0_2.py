import lzma
lzmaPath = 'C:\\Python27\\Lib\site-packages\\lzmaffi-0.1-py2.7-win32.egg\\lzma'

# Open the BZ file
decompressor = lzma.LZMADecompressor()
bz2 = open('tmp01', 'rb')
d = bz2.read()

# BZ decompress
d = decompressor.decompress(d)

print(len(d))
import lzma
lzmaPath = 'C:\\Python27\\Lib\site-packages\\lzmaffi-0.1-py2.7-win32.egg\\lzma'

# Open the BZ file
decompressor = lzma.LZMADecompressor()
bz2 = open('tmp01', 'rb')
d = bz2.read()

# LZ decompress
d = decompressor.decompress(d)
print(len(d))
f = open('decompressed.bz2-001', 'w')
f
