import bz2
# Test BZ2Decompressor as a context manager
with bz2.BZ2Decompressor() as dec:
    with gzip.open(file_name, 'rb') as f:
        data = f.read()
        uncompressed_data = dec.decompress(data)
        print(uncompressed_data[:100])

# Test BZ2File as a context manager
with bz2.BZ2File(file_name) as f:
    for line in f:
        print(line[:50])

# Test BZ2File without context manager
bz2_file = bz2.BZ2File(file_name)
try:
    for line in bz2_file:
        print(line[:50])
finally:
    bz2_file.close()

"""
The BZ2File and BZ2Decompressor classes share a common interface
that is intended to mimic the gzip.open() and gzip.GzipFile() functions
in the standard library

To read compressed data, first create a BZ2File object by passing the name of the
