import lzma
lzma._decompress

# Specialized tests.
_, ext = os.path.splitext(fname)
if ext == '.zstd':
    # Also test non-standard buffer sizes.
    partial = []
    while True:
        buf = fobj.read(5)
        if not buf:
            break
        partial.append(buf)
    for buf in partial:
        fobj.read(buf)

    # Passing a too small buffer to read1() decodes several blocks at once.
    fobj.seek(0)
    fobj.read1(128)
elif ext in ('.lzma', '.xz'):
    # Additional testing for LZMADecompressor that's already tested in
    # test_lzma.
    import lzma
    fobj = lzma.open(fname, 'rb')
    fobj.readline()
    fobj.readline()
    fobj.seek(3)
    fobj.read(1)
    fobj.seek(999)
    fobj.read(
