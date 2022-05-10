import bz2
# Test BZ2Decompressor with multiple decompress() calls
with bz2.BZ2File(filename) as compressed:
    with open(output_filename, 'wt') as uncompressed:
        decompressor = bz2.BZ2Decompressor()
        for block in iter(lambda: compressed.read(100 * 1024), b''):
            uncompressed.write(decompressor.decompress(block))
        uncompressed.write(decompressor.decompress())
    assert decompressor.unused_data == b''

# Test with BZ2File directly
with bz2.BZ2File(filename) as compressed:
    with open(output_filename, 'rb') as uncompressed:
        assert compressed.read() == uncompressed.read()
with open(output_filename, 'rb') as uncompressed:
    assert bz2.decompress(open(filename, 'rb').read()) == uncompressed.read()
