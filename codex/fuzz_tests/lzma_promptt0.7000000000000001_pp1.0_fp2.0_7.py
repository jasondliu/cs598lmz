import lzma
# Test LZMADecompressor

def test_lzma_decompressor():
    cases = (
        (b'', b''),
        (b'\x00', b''),
        (b'\x01\x00', b''),
        (b'\x01\x00\x00\x00\x00', b''),
        (b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00', b''),
        (b'\x00', b'', 0, 0),
        (b'\x00', b'', 0, 1),
        (b'\x00', b'', 1, 0),
        (b'\x00', b'', 0, 2),
        (b'\x00', b'', 2, 0),
        (b'\x00', b'', 1, 2),
        (b'\x00', b'', 2, 1),
        (b'\x00', b'', 2, 2),
        (b'\x00', b'
