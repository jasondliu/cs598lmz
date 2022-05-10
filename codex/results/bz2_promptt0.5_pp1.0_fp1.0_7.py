import bz2
# Test BZ2Decompressor

def test_bz2decompressor():
    with open(TESTFN, 'wb') as f:
        f.write(bz2.compress(b"this is a test of the bz2 module."))
    with open(TESTFN, 'rb') as f:
        d = bz2.BZ2Decompressor()
        un_data = d.decompress(f.read())
        un_data += d.flush()
    assert un_data == b"this is a test of the bz2 module."
    with open(TESTFN, 'rb') as f:
        d = bz2.BZ2Decompressor()
        un_data = d.decompress(f.read(10))
        un_data += d.decompress(f.read())
        un_data += d.flush()
    assert un_data == b"this is a test of the bz2 module."
    with open(TESTFN, 'rb') as f:
        d = bz2.BZ2Decompressor()
       
