import bz2
# Test BZ2Decompressor.decompress(max_length)

compressor = bz2.BZ2Compressor(9)
decompressor = bz2.BZ2Decompressor()

def test(max_length):
    data = compressor.compress(b"a"*100) + compressor.flush()
    got = decompressor.decompress(data, max_length)
    expected = b"a" * max_length
    print(max_length, got == expected)
    return got

test(0)
test(1)
test(2)
test(10)
test(100)
