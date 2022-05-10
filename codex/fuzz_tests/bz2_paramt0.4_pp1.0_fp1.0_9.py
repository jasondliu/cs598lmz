from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# %%
import zlib
zlib.decompress(data)

# %%
import gzip
with open('/tmp/example.txt.gz', 'rb') as f:
    with gzip.open(f) as g:
        text = g.read()
text

# %%
with gzip.open('/tmp/example.txt.gz', 'rt') as g:
    text = g.read()
text

# %%
with open('/tmp/example.txt', 'rt') as f:
    with gzip.open('/tmp/example.txt.gz', 'wt') as g:
        g.write(f.read())

# %%
import bz2
with open('/tmp/example.txt', 'rt') as f:
    with bz2.open('/tmp/example.txt.bz2', 'wt') as b:
        b.write(f.read())

# %%
import lzma
with open('/tmp/example.txt', 'rt') as f:
    with
