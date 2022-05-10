import bz2
# Test BZ2Decompressor with EOFError
try:
    bz2_decomp = bz2.BZ2Decompressor()
    bz2_decomp.decompress(bz2_data + b'garbage')
except EOFError as e:
    print(e)

bz2_decomp = bz2.BZ2Decompressor()
try:
    data = bz2_decomp.decompress(bz2_data)
except:
    pass
print(bz2_decomp.unused_data)

data = b''
bz2_decomp = bz2.BZ2Decompressor()
for chunk in chunks:
    data += bz2_decomp.decompress(chunk)
data += bz2_decomp.flush()
print(data)

# Gzip
import gzip
import io
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

with gzip.open('somefile.gz', 'wt') as f:
    f
