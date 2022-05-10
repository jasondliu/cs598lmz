import lzma
# Test LZMADecompressor.input

def test_input():
    dc = lzma.LZMADecompressor()
    dc.input(compressed)
    output = dc.output()
    assert(output == text)

# Test LZMADecompressor.format_properties

def test_format_properties():
    dc = lzma.LZMADecompressor()
    assert(dc.format_properties == (1, 4))

# Test LZMADecompressor.filter_properties

def test_filter_properties():
    dc = lzma.LZMADecompressor()
    assert(dc.filter_properties == (1, 2, 9))

# Test LZMADecompressor.decompress()

def test_decompress():
    dc = lzma.LZMADecompressor()
    output = dc.decompress(compressed)
    assert(output == text)
