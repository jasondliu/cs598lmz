import bz2
# Test BZ2Decompressor and BZ2Compressor

def test_context_manager(decompressor, data):
    with decompressor as dc:
        assert dc.decompress(data) == b'test'
        assert dc.unused_data == b''
    assert dc.unused_data == b''
    assert dc.eof is True
    raises(EOFError, dc.decompress, b'')

def test_decompressor(decompressor, data):
    assert decompressor.decompress(data) == b'test'
    assert decompressor.unused_data == b''
    decompressor.flush()
    assert decompressor.unused_data == b''
    assert decompressor.eof is True
    raises(EOFError, decompressor.decompress, b'')

def test_decompressor_eof(decompressor, data):
    assert decompressor.decompress(data, eof=True) == b'test'
    assert decompressor.unused_data == b''
    assert decompressor.eof is True
