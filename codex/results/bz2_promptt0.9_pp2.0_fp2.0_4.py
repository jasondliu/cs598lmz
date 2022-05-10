import bz2
# Test BZ2Decompressor
buf = io.BytesIO()
with bz2.BZ2File('data/sample.bz2', mode='wb', compresslevel=9) as f:
    f.write(b'mpoilskjepoilskj')
dec = bz2.BZ2Decompressor()
with open('data/sample.bz2', 'rb') as f:
    while True:
        block = f.read(100)
        if not block:
            break
        uncompress = dec.decompress(block)
        if uncompress:
            print(uncompress)


buf.write(b'mpoilskjepoilskj')
buf.seek(0)
uncompress = dec.decompress(buf.getvalue())
print(uncompress)
