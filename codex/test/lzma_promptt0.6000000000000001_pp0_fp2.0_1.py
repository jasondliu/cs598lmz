import lzma
# Test LZMADecompressor

class TestLZMADecompressor:

    def test_decompress(self):
        c = lzma.LZMADecompressor()
        assert c.decompress(b'') == b''
        assert c.decompress(b'a') == b'a'
        assert c.decompress(b'ab') == b'ab'
        assert c.decompress(b'abc') == b'abc'
        assert c.decompress(b'abcd') == b'abcd'
        assert c.decompress(b'abcde') == b'abcde'
        assert c.decompress(b'abcdef') == b'abcdef'
        assert c.decompress(b'abcdefg') == b'abcdefg'
        assert c.decompress(b'abcdefgh') == b'abcdefgh'
        assert c.decompress(b'abcdefghi') == b'abcdefghi'
