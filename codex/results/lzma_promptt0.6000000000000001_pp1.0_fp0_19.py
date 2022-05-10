import lzma
# Test LZMADecompressor
def test_LZMADecompressor():
    print("LZMADecompressor.decompress")
    data = lzma.compress(b"this is a test")
    fobj = io.BytesIO(data)
    decompressor = lzma.LZMADecompressor()
    assert decompressor.decompress(fobj.read(len(data)//2)) == b""
    assert decompressor.unused_data == b""
    assert decompressor.eof == False
    assert decompressor.decompress(fobj.read()) == b"this is a test"
    assert decompressor.unused_data == b""
    assert decompressor.eof == True
    try:
        decompressor.decompress(b"garbage")
        assert False, "Failed to raise error"
    except EOFError:
        pass
    fobj = io.BytesIO(data)
    decompressor = lzma.LZMADecompressor()
    assert decompressor.decompress(fobj.read(), max_length
