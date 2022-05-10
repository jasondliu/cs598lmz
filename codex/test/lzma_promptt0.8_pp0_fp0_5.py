import lzma
# Test LZMADecompressor

def test_lzma():

    comp = lzma.LZMACompressor()
    data = b"B" * 10**6
    data_comp = comp.compress(data)
    data_comp += comp.flush()
    
    # Check that LZMADecompressor accepts its own output
    dc = lzma.LZMADecompressor()
    data_decomp = dc.decompress(data_comp)
    assert data == data_decomp

def test_lzmaf():
    with lzma.open("make-a-large-file", mode="w") as fh:
        data = b"F" * 10**6
        fh.write(data)

    with lzma.open("make-a-large-file", mode="r") as fh:
        assert data == fh.read()

# Test LZMAFile

