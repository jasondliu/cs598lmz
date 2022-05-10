import bz2
# Test BZ2Decompressor.decompress() with data not ending in an EOF code.

for data in [b'BZ', b'BZ,0', b'BZ,0S', b'BZ,0S\x00']:
    for unused in range(100):
        with bz2.BZ2Decompressor() as dec:
            assert dec.decompress(data) == b''
            assert dec.unused_data == data


# Check that we raise a ValueError if the input isn't terminated by an EOF
# code and we get a BufferError. This should only happen in Python 3.6 and
# earlier.
for input in [b'BZ,0\x00\x00']:
    dec = bz2.BZ2Decompressor()
    dec.decompress(input)
    dec.flush()
    with pytest.raises(ValueError):
        dec.unused_data
