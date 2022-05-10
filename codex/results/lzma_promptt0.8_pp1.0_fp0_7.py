import lzma
# Test LZMADecompressor object with all kinds of input lengths, including
# zero-length data, and make sure that the right number of output bytes
# are returned.

import lzma

def test_decompressor(data, expected):
    d = lzma.LZMADecompressor()
    have = b""
    while True:
        chunk = d.decompress(data)
        if chunk:
            have += chunk
        else:
            break
    if have != expected:
        print(len(have), len(expected))
        assert have == expected

def test_decompressor_eof(data, expected):
    d = lzma.LZMADecompressor()
    have = b""
    while True:
        chunk = d.decompress(data, 512)
        if chunk:
            have += chunk
        else:
            break
    if have != expected:
        print(len(have), len(expected))
        assert have == expected

def test_decompressor_flush(data, expected):
    d = lzma.LZM
