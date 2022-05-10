import lzma
# Test LZMADecompressor and LZMACompressor by compression and decompression of
# random data; the data should come out in exactly the same form as at input.

for i in range(100):
    data = os.urandom(i)

    c  = lzma.LZMACompressor()
    d = lzma.LZMADecompressor()

    compressed = b''
    for i in range(0, len(data), 100):
        compressed += c.compress(data[i:i+100])

    compressed += c.flush()

    print(len(compressed), len(data))
    assert len(compressed) > 0
    decompressed = d.decompress(compressed)
    assert decompressed == data
# Test that LZMA filters can be used directly
# in a compression pipeline

for i in range(100):
    data = os.urandom(i)

    c = lzma.LZMACompressor(lzma.FORMAT_XZ)
    f = lzma.FILTER_LZMA1(preset=7)

