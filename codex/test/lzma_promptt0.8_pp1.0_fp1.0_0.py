import lzma
# Test LZMADecompressor.multistream
UNUSED = frozenset(range(256)) - frozenset(b'ABCDEFGHIJKLMNOPQRSTUVWX1YZ2:01\x00')
DATA1 = b'A' * 256    # must be distinct from DATA2
DATA2 = b'B' * 256    # must be distinct from DATA1
