import lzma
# Test LZMADecompressor

def test_lzma():
    cdata = lzma.compress(b"abc")
    with lzma.LZMADecompressor() as dec:
        assert dec.decompress(cdata) == b"abc"

# Test LZMACompressor and LZMADecompressor

def test_lzma_comp_decomp():
    # the last byte of the compressed output makes it fail without the fix
    data = b"x" * 100 + b"a" * 16 + b"\x00"
    with lzma.LZMACompressor() as comp:
        cdata = comp.compress(data)
        cdata += comp.flush()
    with lzma.LZMADecompressor() as decomp:
        assert decomp.decompress(cdata) == data

def test_lzma_decomp_with_no_flush():
    data = b"x" * 100 + b"a" * 16 + b"\x00"
    with lzma.LZMACompressor() as
