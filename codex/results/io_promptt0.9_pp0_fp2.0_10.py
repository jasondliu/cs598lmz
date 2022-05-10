import io
# Test io.RawIOBase.readall() in particular
# (issue12543).
if hasattr(io.RawIOBase, "readall"):
    gc.disable()
    # Create an instance of a RawIOBase subclass with a readall() method
    f = gzip.GzipFile(__file__)
    f.readall()
# skip closing files explicitly
def test_exhausted_read():
    import sys
    import io
    if hasattr(sys.stdin, 'mode'):
        # sys.stdin.mode may be defined but not sys.stdin.buffer.
        # For example, if sys.stdin is io.StringIO.
        stdin = io.TextIOWrapper(io.ByteIO(b"abcdef"), encoding="utf-8")
    else:
        stdin = io.BytesIO(b"abcdef")
    for meth_name in ['read', 'read1']:
        meth = getattr(stdin, meth_name)
        for i in range(4):
            # Even though the underlying buffer is exhausted, the
            # Text
