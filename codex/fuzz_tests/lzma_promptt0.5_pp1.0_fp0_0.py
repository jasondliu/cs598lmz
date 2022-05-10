import lzma
# Test LZMADecompressor.decompress()

def test_decompress():
    # Decompress a file compressed with xz -1
    with open('testdata/lzma-1.xz', 'rb') as f:
        comp = lzma.LZMADecompressor()
        with open('testdata/lzma-1.txt', 'rb') as f2:
            assert f2.read() == comp.decompress(f.read())

def test_decompress_incomplete():
    # Decompress a file compressed with xz -1
    with open('testdata/lzma-1.xz', 'rb') as f:
        comp = lzma.LZMADecompressor()
        with open('testdata/lzma-1.txt', 'rb') as f2:
            assert f2.read()[:50] == comp.decompress(f.read()[:50])

def test_decompress_incomplete_eos():
    # Decompress a file compressed with xz -1
    with
