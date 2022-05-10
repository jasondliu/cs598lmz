import bz2
# Test BZ2Decompressor and BZ2Compressor.

# Note, when using the binary file mode, \n is converted to the
# the local line separator.  So on Windows, the
# BZ2Decompressor returns binary data.


data = b"hello to compression and decompression" * 50
print('data is %d bytes' % len(data))

for i in range(1, 10):
    print('Test %d ---------------' % i)
    c = bz2.BZ2Compressor(i)
    d = bz2.BZ2Decompressor()
    assert d.unused_data == b''
    result = b''
    result = c.compress(data)
    result += c.flush()
    print('Compressed from %d to %d' % (len(data), len(result)))
    result2 = d.decompress(result)
    result2 += d.flush()
    assert d.unused_data == b''
    assert result2 == data
    assert len(result2) == len(data)


def test_invalid
