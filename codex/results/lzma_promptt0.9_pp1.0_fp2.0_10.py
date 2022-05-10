import lzma
# Test LZMADecompressor on a few bytes of input


VALID_INPUTS = [
        b'somenonsense',
        b'12345678' * 100000,
        ]

INVALID_INPUTS = [
        b'123456',
        b'1234567891011',
        b'12345678' * 99999,
        # A single byte of an xz/lzma stream contains either
        #   (1) a single byte of data
        #   (2) an "end marker" that signals the end of the data stream
        # In order to make 
        b'\x00\x00\x00\x00\x00\x00\x00\x00',
        ]

def test_decompressor():
    for data in VALID_INPUTS:
        d = lzma.LZMADecompressor()
        decompressed = d.decompress(data)
        print(b"Testing decompression of %d bytes gives %d" % (len(data), len(decompressed)))
        assert len(data) * 2
