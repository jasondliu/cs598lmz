import lzma
# Test LZMADecompressor modes

class TestLZMA(unittest.TestCase):
    def test_decompressor(self):
        d = lzma.LZMADecompressor()
        for data, result in (
                (b'', b''),
                (b'\x00', b''),
                (b'\x00', b''),
                (b'\x00\x00', b''),
                (b'\x00\x00\x00', b''),
                (b'\x00\x00\x00\x00', b''),
                (b'\x00\x00\x00\x00\x00', b''),
                (b'\x00\x00\x00\x00\x00\x01', b'\x00'),
                (b'\x00\x00\x00\x00\x00\x01\x00', b'\x00'),
                (b'\x00\x00\x00\x00\x00\x01\x01', b'\x
