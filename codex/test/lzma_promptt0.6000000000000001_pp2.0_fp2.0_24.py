import lzma
# Test LZMADecompressor
# https://docs.python.org/3/library/lzma.html

def test_lzma():
    bytes_in = b"testing testing 1 2 3"
    comp = lzma.LZMACompressor()
    bytes_out = comp.compress(bytes_in)
    bytes_out += comp.flush()

    decomp = lzma.LZMADecompressor()
    bytes_decomp = decomp.decompress(bytes_out)

    assert bytes_decomp == bytes_in


# Test LZMADecompressorStream
# https://www.python.org/dev/peps/pep-0495/

def test_lzma_stream():
    bytes_in = b"testing testing 1 2 3"
    comp = lzma.LZMACompressor()
    bytes_out = comp.compress(bytes_in)
    bytes_out += comp.flush()

    decomp = lzma.LZMADecompressorStream()
    bytes_decomp = decomp.decompress(bytes_out)
