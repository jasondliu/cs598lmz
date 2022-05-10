import lzma
# Test LZMADecompressor and LZMACompressor with various settings.

def test_decompressor():
    # Test the decompressor with various settings.
    data = b'x' * 100000
    for preset in range(0, 9):
        for eos in (False, True):
            compressed = lzma.compress(data, preset=preset, eos=eos)
            for check in range(lzma.CHECK_NONE, lzma.CHECK_ID_MAX + 1):
                decomp = lzma.LZMADecompressor(format=lzma.FORMAT_RAW,
                                               check=check)
                decompressed = decomp.decompress(compressed)
                assert decompressed == data
                assert decomp.eof is eos
                assert decomp.unused_data == b''
                assert decomp.decompress(b'x') == b''
                assert decomp.unused_data == b'x'
                assert decomp.decompress(b'x', max_length=0) == b''
                assert decomp.unused_data == b
