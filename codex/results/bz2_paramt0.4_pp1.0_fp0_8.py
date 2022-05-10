from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# bz2.open()
with bz2.open('file.bz2', 'rt') as f:
    data = f.read()
