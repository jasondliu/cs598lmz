import lzma
# Test LZMADecompressor with a known file

def test_lzma_decompressor():
    input_file = open('test/testdata/lorem_ipsum.xz', 'rb')
    decompressor = lzma.LZMADecompressor()
    assert decompressor.eof == False
    output = decompressor.decompress(input_file.read())
    assert decompressor.eof == True
    assert output == b'Lorem ipsum dolor sit amet, consectetur adipiscing elit.\n'

def test_lzma_decompressor_eof():
    input_file = open('test/testdata/lorem_ipsum.xz', 'rb')
    decompressor = lzma.LZMADecompressor()
    assert decompressor.eof == False
    output = decompressor.decompress(input_file.read(), max_length=50)
    assert decompressor.eof == False
    assert output == b'Lorem ipsum dolor sit amet, consectetur ad'
    output =
