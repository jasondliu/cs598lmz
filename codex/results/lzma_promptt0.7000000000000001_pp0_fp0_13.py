import lzma
# Test LZMADecompressor(format=FORMAT_AUTO)
def test_lzma_auto_fileobj():
    with open('liblzma.src/xz/doc/examples/compress/alice29.txt', 'rb') as f:
        comp = lzma.LZMADecompressor(format=lzma.FORMAT_AUTO)
        data = f.read()
        data_decomp = comp.decompress(data)
        with open('liblzma.src/xz/doc/examples/compress/alice29.txt', 'rb') as f:
            assert data_decomp == f.read()

# Test LZMADecompressor(format=FORMAT_ALONE)
def test_lzma_alone():
    # The xz utils don't add the end marker by default, so use
    # test files that have been processed by xz -9.
    with open('liblzma.src/xz/doc/examples/compress/alice29.txt.xz', 'rb') as f
