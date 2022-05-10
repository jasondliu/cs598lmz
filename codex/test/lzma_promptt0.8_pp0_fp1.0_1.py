import lzma
# Test LZMADecompressor and LZMACompressor.

def test_LZMADecompressor_fileobj_interface(filetest):
    data = filetest.get_data()
    filetest.test_file_interface(lzma.LZMADecompressor, data)

def test_LZMADecompressor_no_eof(filetest):
    data = filetest.get_data()
    with lzma.LZMADecompressor() as d:
        assert d.unused_data == b''
        decomp = d.decompress(data)
        assert d.unused_data == b''
        assert len(decomp) > 0
        assert not d.eof
        assert d.unused_data == b''
        assert d.decompress(b'') == b''
        assert d.eof
        assert d.unused_data == b''
        assert d.decompress(b'not empty') == b''
        assert d.eof
        assert d.unused_data == b'not empty'
