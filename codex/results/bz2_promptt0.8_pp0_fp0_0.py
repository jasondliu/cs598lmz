import bz2
# Test BZ2Decompressor.decompress() with various inputs

for i in range(100):
    data = b"".join(chr(random.randrange(0, 256)) for _ in range(i))
    compressed = bz2.compress(data)

    d = bz2.BZ2Decompressor()
    output = d.decompress(compressed)
    assert output == data
    assert len(d.unused_data) == 0

    d = bz2.BZ2Decompressor()
    output = d.decompress(compressed[:5])
    assert output[:5] == data[:5]
    output += d.decompress(compressed[5:])
    assert output == data
    assert len(d.unused_data) == 0

    d = bz2.BZ2Decompressor()
    output = d.decompress(compressed[:5] + compressed[-5:])
    assert output == data
    assert len(d.unused_data) == 10

    d = bz2.BZ2
