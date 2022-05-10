import bz2
# Test BZ2Decompressor's readline() implementation against the same data 
# decompressed using bz2.decompress() and bz2.BZ2Decompressor.

NUM_LINES = 10000

data = bz2.decompress(bz2.compress(b'data '*NUM_LINES))

for decomp in [bz2.BZ2Decompressor(), BZ2Decompressor()]:
    stream = BytesIO(data)
    dec = decomp.decompress(stream.read())
    lines = dec.split(b'\n')
    incr = BytesIO(dec)
    for i in range(NUM_LINES):
        assert decomp.readline() == lines[i] + b'\n'
        assert decomp.readline() == lines[i+1] + b'\n'
        assert incr.readline() == lines[i] + b'\n'
        assert incr.readline() == lines[i+1] + b'\n'
    assert not incr.read()
    assert decomp.readline()
