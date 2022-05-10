import bz2
# Test BZ2Decompressor
data = b'BZh91AY&SY.\xc8N\x18\x00\x01>_\x80\x00\x10@\x02\xff\xf0\x01\x07n\x00?'

compressor = bz2.BZ2Decompressor()
compressor.decompress(data)

# Test BZ2Decompressor.flush()
for c in compressor.decompress(data):
    print(c)
compressor.flush()

# Test BZ2Compressor
compressor = bz2.BZ2Compressor()
compressor.compress(b"this is a test")
compressor.flush()

# Test BZ2File
with bz2.open(bz2_filename, mode='wt') as f:
    f.write('this is a test')

with bz2.open(bz2_filename, mode='rt') as f:
    print(f.read())

with bz2.open(bz2_filename, mode='wt') as f:

