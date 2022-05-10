import lzma
# Test LZMADecompressor.multistream
UNUSED = frozenset(range(256)) - frozenset(b'ABCDEFGHIJKLMNOPQRSTUVWX1YZ2:01\x00')
DATA1 = b'A' * 256    # must be distinct from DATA2
DATA2 = b'B' * 256    # must be distinct from DATA1
with lzma.LZMACompressor(check=lzma.CHECK_CRC64) as comp:
    comp1 = comp.compress(DATA1)
    comp1 += comp.compress(DATA1)
    comp2 = comp.compress(DATA2)
    comp2 += comp.compress(DATA2)
    comp3 = comp.compress(DATA1)
    comp3 += comp.compress(DATA2)
    enc = lzma.LZMADecompressor.multistream(comp1 + comp2 + comp3)
    test.support.unlink(test.TESTFN)
    with test.support.open_helper(test.TESTFN) as f:
       
