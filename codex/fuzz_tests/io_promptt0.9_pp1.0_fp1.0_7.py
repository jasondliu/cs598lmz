import io
# Test io.RawIOBase subclassing
with io.BytesIO('s') as f:
    with io.BytesIO('t') as g:
        f.seek(0)
        g.seek(0)
        isinstance(f, io.RawIOBase)

# Test io.BufferedIOBase subclassing
with io.BytesIO('s') as f:
    with io.BytesIO('t') as g:
        f.seek(0)
        g.seek(0)
        isinstance(f, io.BufferedIOBase)

# Test io.TextIOBase subclassing
with io.StringIO('s') as f:
    with io.StringIO('t') as g:
        f.seek(0)
        g.seek(0)
        isinstance(f, io.TextIOBase)

# Test BlockingIOError subclassing
with io.BytesIO('s') as f:
    f.seek(0)
    isinstance(BlockingIOError(1, 'x', 2, None), BlockingIOError)

with io.BytesIO('s') as f:
