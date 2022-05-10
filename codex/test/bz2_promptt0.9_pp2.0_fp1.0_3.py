import bz2
# Test BZ2Decompressor with short streams containing no compressed data
# and see if it returns empty strings or raises EOFError.
decomp = bz2.BZ2Decompressor()
assert decomp.decompress(b'') == b''
assert decomp.decompress(b'') == b''

