import lzma
# Test LZMADecompressor

def test_LZMADecompressor():
    for i in range(256):
        c = lzma.LZMADecompressor()
        assert c.decompress(bytes([i])) == b''
        assert c.unused_data == bytes([i])
        assert c.eof is False
        assert c.needs_input is True
        assert c.needs_input is True
        assert c.flush() == b''
        assert c.unused_data == b''
        assert c.eof is False
        assert c.needs_input is True
        assert c.needs_input is True
        assert c.decompress(b'') == b''
        assert c.unused_data == b''
        assert c.eof is False
        assert c.needs_input is True
        assert c.needs_input is True
        assert c.flush() == b''
        assert c.unused_data == b''
        assert c.eof is False
        assert c.needs_input is True
        assert c.needs_input is True
