import bz2
# Test BZ2Decompressor with short streams containing no compressed data
# and see if it returns empty strings or raises EOFError.
decomp = bz2.BZ2Decompressor()
assert decomp.decompress(b'') == b''
assert decomp.decompress(b'') == b''

with pytest.raises(EOFError):
    decomp.decompress(b'x')

decomp = bz2.BZ2Decompressor()
assert decomp.decompress(b'x') == b'x'

with pytest.raises(EOFError):
    decomp.decompress(b'x')
# Test that BZ2Decompressor objects cannot be copied.
decomp = bz2.BZ2Decompressor()
with pytest.raises(TypeError):
    copy.copy(decomp)

with pytest.raises(TypeError):
    copy.deepcopy(decomp)
# Test that BZ2Decompressor objects support the context management protocol.
with bz2.BZ2Decompressor() as decomp:
    pass
