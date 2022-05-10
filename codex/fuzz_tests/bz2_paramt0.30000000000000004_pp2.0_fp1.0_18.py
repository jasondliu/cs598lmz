from bz2 import BZ2Decompressor
BZ2Decompressor().decompress(data)

# bz2.BZ2File
with bz2.BZ2File('file.txt.bz2') as f:
    data = f.read()

# bz2.decompress
bz2.decompress(data)

# bz2.open
with bz2.open('file.txt.bz2') as f:
    data = f.read()

# bz2.decompress
bz2.decompress(data)

# bz2.open
with bz2.open('file.txt.bz2') as f:
    data = f.read()

# bz2.BZ2Decompressor
with open('file.txt.bz2', 'rb') as f:
    data = f.read()

with io.BytesIO(data) as bio:
    with bz2.BZ2Decompressor() as bz:
        data = bz.decompress(bio.read())

# bz2.BZ2
