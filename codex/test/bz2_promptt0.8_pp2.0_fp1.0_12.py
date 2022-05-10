import bz2
# Test BZ2Decompressor
def check_bz2decompressor_state():
    for state in range(1, 16):
        d = bz2.BZ2Decompressor(state)
        try:
            d.decompress(b"something")
        except ValueError:
            pass
        else:
            assert False, "Should have raised ValueError"

# Test BZ2Decompressor with a real bz2-compressed file
def check_bz2decompressor_compressedfile():
    txt = open(TESTFN, 'rb').read()
    with open(TESTFN, 'rb') as f:
        fcomp = bz2.BZ2File(f)
        fcomp.seek(0)
        z = fcomp.read()
    d = bz2.BZ2Decompressor()
    result = d.decompress(z)
    result += d.flush()
    assert len(result) == len(txt)
    assert result == txt

# Test BZ2Decompressor with numerous bz2-compressed files

