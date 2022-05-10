import lzma
# Test LZMADecompressor and LZMACompressor classes

def test_decompressor_interface():
    decompressor = lzma.LZMADecompressor()
    assert not decompressor.eof
    with pytest.raises(IOError):
        decompressor.decompress(b'blah')
    data = b'lzma12345678901234'
    compressed = lzma.compress(data)
    decompressed = decompressor.decompress(compressed)
    assert len(decompressed) == len(data)
    assert decompressed == data

    decompressed = decompressor.decompress(compressed[:1])
    assert len(decompressed) == 0
    decompressed = decompressor.decompress(compressed[1:2])
    assert len(decompressed) == 1
    decompressed = decompressor.decompress(compressed[2:3])
    assert len(decompressed) == 2
    decompressed = decompressor.decompress(compressed[3:4])
    assert len(decompressed) == 3

   
