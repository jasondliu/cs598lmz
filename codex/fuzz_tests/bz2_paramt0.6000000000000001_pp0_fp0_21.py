from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2.compress(data)) == data

#%%
from bz2 import compress, decompress
compress(b"Hello world!")
decompress(b"BZh91AY&SYA\xaf\x82\r\x00\x00\x01\x01\x80\x02\xc0\x02\x00 \x00!\x9ah3M\x07<]\xc9\x14\xe1BA\x06\xbe\x084")

#%%
import gzip
s = b'witch which has which witches wrist watch'
len(s)
t = gzip.compress(s)
len(t)
gzip.decompress(t)
gzip.compress(s) == t

#%%
import gzip
with gzip.open('file.txt.gz', 'wt') as f:
    f.write(text)

with gzip.open('file.txt.gz', 'rt') as f:
    text = f.read()

#%%
