import lzma
# Test LZMADecompressor.decompress using data from lzma.LZMAEncoder
for COMPRESSLEVEL in range(1,10):
    CLEVEL = COMPRESSLEVEL
    print (CLEVEL)
    enc = lzma.LZMAEncoder(CLEVEL, 'LZMA_MODE_NORMAL')
    for data in [b'a' * 100 + b'bbbb', b'a' * 100 + b'bbbb', b'a' * 100 + b'bbaa', b'a' * 100 + b'bbcc']:
        data = enc.encode(data)
        if len(data) < 10:
            print(data)
            continue
        d = lzma.LZMADecompressor()
        # Before we can decompress anything, we must use
        # LZMADecompressor.decompress(return_check=True) to feed in some header
        header = d.decompress(data, return_check=True)
        # A positive return value indicates that the header was successfully
        # checked.
        if header > 0:
