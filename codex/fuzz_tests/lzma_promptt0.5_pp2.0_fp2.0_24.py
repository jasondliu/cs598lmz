import lzma
# Test LZMADecompressor.format_error()

def check_error(err, msg):
    if err.msg != msg:
        raise Exception("Expected: %r, got %r" % (msg, err.msg))

def test_format_error():
    # Test LZMADecompressor.format_error()
    c = lzma.LZMADecompressor()
    c.eof = True
    c.unconsumed_tail = b'abcdefg'
    c.decompress(b'abcdefg')
    check_error(c.decompress(b'abcdefg'), "Error -3 while decompressing: invalid literal/length or distance code")
    c.decompress(b'abcdefg')
    check_error(c.decompress(b'abcdefg'), "Error -3 while decompressing: invalid literal/length or distance code")
    c.decompress(b'abcdefg')
    check_error(c.decompress(b'abcdefg'), "Error -3 while decompressing: invalid literal/length or distance code
