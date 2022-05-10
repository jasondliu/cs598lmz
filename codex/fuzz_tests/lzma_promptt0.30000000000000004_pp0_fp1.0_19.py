import lzma
# Test LZMADecompressor

# Test that the decompressor can be used in a with statement
with lzma.LZMADecompressor() as decomp:
    assert decomp.eof is False
    assert decomp.unused_data == b''
    assert decomp.decompress(b'\x00') == b''
    assert decomp.eof is False
    assert decomp.unused_data == b''
    assert decomp.decompress(b'\x00') == b''
    assert decomp.eof is False
    assert decomp.unused_data == b''
    assert decomp.decompress(b'\x00') == b''
    assert decomp.eof is False
    assert decomp.unused_data == b''
    assert decomp.decompress(b'\x00') == b''
    assert decomp.eof is False
    assert decomp.unused_data == b''
    assert decomp.decompress(b'\x00') == b''
    assert decomp.eof is False
    assert decomp.unused_data == b''
    assert decomp.decompress
