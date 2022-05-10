import bz2
# Test BZ2Decompressor with streaming

with open("sample1.bz2", "rb") as f:
    d = bz2.BZ2Decompressor()
    for chunk in iter(lambda: f.read(100), b""):
        data = d.decompress(chunk)
        if data:
            print(data)

# Test BZ2Decompressor with single decompress call

with open("sample1.bz2", "rb") as f:
    d = bz2.BZ2Decompressor()
    print(d.decompress(f.read()))

# Test BZ2Decompressor decompress with multiple calls

with open("sample1.bz2", "rb") as f:
    d = bz2.BZ2Decompressor()
    print(d.decompress(f.read(100)))
    print(d.decompress(f.read()))

# Test BZ2Decompressor decompress for multiple files

with open("sample1.bz2", "rb") as f1, open("sample
