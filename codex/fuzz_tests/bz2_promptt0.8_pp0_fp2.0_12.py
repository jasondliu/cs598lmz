import bz2
# Test BZ2Decompressor
def test_bz2decompressor():
    with bz2.BZ2Decompressor() as decomp:
        assert decomp.unconsumed_tail == b''
        assert decomp.decompress(b'data') == b'data'
        assert decomp.unconsumed_tail == b''
        assert decomp.decompress(b'\x42\x5a\x68\x39\x31\x41\x59\x26\x53\x59'
                                 b'\xab\x42\x00\x00\x00') == b'foo'
        assert decomp.unconsumed_tail == b''
