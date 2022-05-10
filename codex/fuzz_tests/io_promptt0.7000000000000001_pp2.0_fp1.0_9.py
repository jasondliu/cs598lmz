import io
# Test io.RawIOBase subclass
try:
    from io import BytesIO as IO
except ImportError:
    from io import StringIO as IO  # python 3.x

# Test basic I/O
print("*** raw string ***")
for i in range(10):
    raw = gen_raw(i)
    print("raw len = %d" % len(raw), end=' ')
    compressed = compress(raw)
    print("compressed len = %d" % len(compressed), end=' ')
    decompressed = decompress(compressed)
    print("decompressed len = %d" % len(decompressed), end=' ')
    print()
    assert raw == decompressed

print("*** random string ***")
for i in range(10):
    raw = gen_random(i)
    print("raw len = %d" % len(raw), end=' ')
    compressed = compress(raw)
    print("compressed len = %d" % len(compressed), end=' ')
    decompressed = decompress(compressed)
    print("decompressed len
