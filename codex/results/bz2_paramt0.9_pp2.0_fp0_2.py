from bz2 import BZ2Decompressor
BZ2Decompressor.decompress(b)

b"YELLOW SUBMARINE"

b2s = b[:]
with BZ2Decompressor() as decomp:
    for i in range(len(b2s)):
        b2s = b2s[:i] + decomp.decompress(b2s[i:])

b2s

b2s == b"YELLOW SUBMARINE"
