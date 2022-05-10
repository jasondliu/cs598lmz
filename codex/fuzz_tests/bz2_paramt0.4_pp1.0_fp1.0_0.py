from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(bz2_data)

# bz2.decompress()
bz2.decompress(bz2_data)

# bz2.open()
with bz2.open('file.bz2') as f:
    f.read()

# bz2.BZ2File()
with bz2.BZ2File('file.bz2') as f:
    f.read()

# bz2.BZ2File() + read()
with open('file.bz2', 'rb') as f:
    f.read()
