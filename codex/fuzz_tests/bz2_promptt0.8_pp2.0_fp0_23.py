import bz2
# Test BZ2Decompressor

with bz2.BZ2File('compressed.bz2', 'r') as bz2file:
    stream = io.BytesIO(bz2file.read())

with bz2.BZ2File('compressed.bz2', 'r') as bz2file:
    for line in bz2file:
        print(line)

with bz2.open('compressed.bz2', 'rt') as bz2file:
    for line in bz2file:
        print(line)

bz2file = bz2.open('compressed.bz2', 'rt')
for line in bz2file:
    print(line)
bz2file.close()


# to get a string we need to decode
with bz2.open('compressed.bz2', 'rt') as bz2file:
    for line in bz2file:
        print(line.decode('latin-1'))

# Encoding and Decompression
encdec = bz2.BZ2
