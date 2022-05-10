import bz2
# Test BZ2Decompressor object
with open('sample_data/sample.bz2', 'rb') as input:
    decompressor = bz2.BZ2Decompressor()
    for block in iter(lambda: input.read(100 * 1024), b''):
        data = decompressor.decompress(block)
        # ... process data ...
        if not data:
            break
    leftover = decompressor.decompress(b"")
    leftover += decompressor.flush()
    # ... process leftover ...
    # Check that we've reached the end of the compressed data
    remaining_data = input.read()
    # ...
# The BZ2File class provides a convenient way to wrap a compressed file
# inside an on-disk file.
with bz2.BZ2File('sample_data/sample.bz2', 'rb') as input:
    for line in input:
        print(line)
# The same code using a decompression object
with open('sample_data/sample.bz2', 'rb') as input:
    with bz2.open(input, 'rb') as decomp
