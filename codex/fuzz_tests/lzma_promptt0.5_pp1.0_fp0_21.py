import lzma
# Test LZMADecompressor
with lzma.open("./data/enwik8", "rb") as f:
    d = lzma.LZMADecompressor()
    data = f.read(10)
    while data:
        print(d.decompress(data))
        data = f.read(10)

# Test LZMAFile
with lzma.open("./data/enwik8", "rb") as f:
    print(f.read(10))

# Test LZMAFile with filters
filters = [
    {"id": lzma.FILTER_LZMA2, "preset": 9 | lzma.PRESET_EXTREME},
    {"id": lzma.FILTER_DELTA, "dist": 4},
]
with lzma.open("./data/enwik8", "rb", filters=filters) as f:
    print(f.read(10))
