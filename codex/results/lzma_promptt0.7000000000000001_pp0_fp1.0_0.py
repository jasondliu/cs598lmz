import lzma
# Test LZMADecompressor
decomp = lzma.LZMADecompressor()
with lzma.open('data/enwik8.xz') as comp_file:
    raw = comp_file.read()
    decomp.decompress(raw)
    len(decomp.unused_data)

decomp = lzma.LZMADecompressor()
with lzma.open('data/enwik8.xz') as comp_file:
    raw = comp_file.read()
    decomp.decompress(raw)
    len(decomp.unused_data)
    decomp.decompress(decomp.unused_data)
    len(decomp.unused_data)
with lzma.open('data/enwik8.xz') as comp_file:
    decomp = lzma.LZMADecompressor()
    with open('data/enwik8.txt', 'wb') as out_file:
        while True:
            decompressed = decomp.decompress(comp_file.read(50000))
            if
