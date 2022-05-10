import lzma
# Test LZMADecompressor.read() method

def write_read_decompressor(data, chunksize=1):
    compressor = lzma.LZMACompressor()
    compressed = compressor.compress(data)
    compressed += compressor.flush()
    #print(len(compressed))
    decompressor = lzma.LZMADecompressor()
    dec = b''
    for i in range(0, len(compressed), chunksize):
        dec += decompressor.decompress(compressed[i:i+chunksize])
    dec += decompressor.flush()
    return dec

def test_lzma_read():
    # This data is a random string encoded with xz -1 with xz 5.1.2alpha.
    # The xz 5.1.2alpha has a bug in the LZMA2 code that causes the
    # decompressor to fail to decompress this data. The bug has been fixed
    # in xz 5.1.2beta.
    data = b'\xfd7zXZ\x00\x04\xe6\xd
