import lzma
# Test LZMADecompressor.decompress() method by comparing output
# to the uncompressed test file.

# Prepare test data: read the whole test-file.lzma first.
xzf = open('../test/test-corpus/test-file.lzma', 'rb')
try:
    data = xzf.read()
finally:
    xzf.close()

# Try to decompress using 1, 2 and 5 bytes at a time... 
for chunksize in (1, 2, 5, 200):
    xzd = lzma.LZMADecompressor()
    result = []
    data_offset = 0
    while True:
        # Subsequent calls to decompress() must use the unused data... 
        chunk = data[data_offset:data_offset + chunksize]
        if not chunk:
            break
        try:
            d = xzd.decompress(chunk)
        except lzma.LZMAError:
            raise
            # Try to work around bugs in LZMADecompressor.decompress() in
