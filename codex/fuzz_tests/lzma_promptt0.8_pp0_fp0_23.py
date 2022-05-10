import lzma
# Test LZMADecompressor.seek()

data = b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'

def test_seek():
    for bufsize in range(1, 22):
        for offset in range(23):
            # "Seeking" to offset 0 should reset the decompressor
            decompressor = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE, filters=[{"id": lzma.FILTER_X86, "preset": 9 | lzma.PRESET_EXTREME}])
            # Fill input buffer
            decompressor.decompress(b'\x00', bufsize)
            # Seek backward
            decompressor.seek(-offset, 1)
            # Decompress the same data again
            assert decompressor.decompress(data, 50) == data

            # "Seek" to the beginning
            decompressor2 = lzma.LZMADecompressor(format=lzma.FORMAT_ALONE, filters=[
