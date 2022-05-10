import bz2
# Test BZ2Decompressor.extrabuf
class TestBZ2Decompressor:
    def test_extrabuf_many_writes(self):
        comp = bz2.BZ2Decompressor()
