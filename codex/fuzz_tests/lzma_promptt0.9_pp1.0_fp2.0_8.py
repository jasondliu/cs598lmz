import lzma
# Test LZMADecompressor
def test_lzma_decompressor(filename):
    with open(filename, "rb") as fi:
        comp = lzma.LZMADecompressor()
        b = BytesIO(fi.read())
        # use read() in chunks instead of readall() will save some space
        data = b''
        while True:
            next_chunk = b.read(1024 * 1024 * 10)
            if not next_chunk:
                break
            d = comp.decompress(next_chunk)
            data += d
    print(len(data))
# Test LZMACompressor
def test_lzma_compressor(filename):
    with open(filename, "rb") as fi:
        comp = lzma.LZMACompressor()
        b = BytesIO(fi.read())
        # use read() in chunks instead of readall() will save some space
        data = BytesIO()
        while True:
            next_chunk = b.read(1024 * 1024 * 10)
            if not next_chunk:
