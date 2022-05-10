import lzma
# Test LZMADecompressor.readinto()

orig_data = b"This is a test string!\n"

for filters in [
        [{"id": lzma.FILTER_LZMA1, "dict_size": 4096, "lc": 3, "lp": 0, "pb": 2, "mode": lzma.MODE_FAST}],
        [{"id": lzma.FILTER_LZMA1, "dict_size": 4096, "lc": 3, "lp": 0, "pb": 2, "mode": lzma.MODE_NORMAL}]]:
    print("Filters:", filters)
    # Test the case where the destination buffer is large enough.
    data = lzma.compress(orig_data, format=lzma.FORMAT_RAW, filters=filters)
    assert len(data) > 0
    decomp = lzma.LZMADecompressor()
    buf = bytearray(len(orig_data))
    assert decomp.readinto(buf) == len(orig_data)
    assert buf == orig_data
   
