import lzma
# Test LZMADecompressor
with lzma.LZMADecompressor() as dec:
    with lzma.open("bad_lzma_data.file") as f:
        data = f.read()
        print(dec.decompress(data))


# Test LZMAFile
with lzma.open("bad_lzma_data.file") as f:
    data = f.read()
    print(data)


# Test open_maybe_compressed
with open_maybe_compressed("bad_lzma_data.file") as f:
    data = f.read()
    print(data)
