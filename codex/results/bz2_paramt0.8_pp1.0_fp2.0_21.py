from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

from gzip import GzipFile
from io import BytesIO
with GzipFile(fileobj=BytesIO(data)) as f:
    text = f.read()

# To compress
from bz2 import BZ2Compressor
with open('text.txt.bz2', 'wb') as f:
    f.write(BZ2Compressor().compompress(text))

with open('text.txt.gz', 'wb') as f:
    f.write(GzipFile('text.txt', 'wb').compompress(text))

# zlib
import zlib
s = b'witch which has which witches wrist watch'
len(s)

t = zlib.compress(s)
len(t)

zlib.decompress(t)

zlib.crc32(s)

# struct
i = 10240099
b1 = (i & 0xff000000) >> 24
b2 = (i & 0xff0000) >> 16
b3 = (i & 0xff00) >> 8

