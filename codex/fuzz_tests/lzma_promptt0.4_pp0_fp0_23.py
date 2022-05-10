import lzma
# Test LZMADecompressor

# Test decompression of a file that is not compressed with LZMA
def test_bad_file():
    with pytest.raises(lzma.LZMAError):
        with open('testdata/bad.xz', 'rb') as f:
            d = lzma.LZMADecompressor()
            d.decompress(f.read())

# Test decompression of a file that is not compressed with LZMA
def test_bad_file_2():
    with pytest.raises(lzma.LZMAError):
        with open('testdata/bad.xz', 'rb') as f:
            d = lzma.LZMADecompressor()
            d.decompress(f.read())

# Test decompression of a file that is not compressed with LZMA
def test_bad_file_3():
    with pytest.raises(lzma.LZMAError):
        with open('testdata/bad.xz', 'rb') as f:
            d = lzma.LZ
