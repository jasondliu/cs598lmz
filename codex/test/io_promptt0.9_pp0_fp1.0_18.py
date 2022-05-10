import io
# Test io.RawIOBase docstring
# %sending:11
# %receiving:12
buf = io.BytesIO(b"spam\n")
r = io.TextIOWrapper(buf)
r.readable()
# %sending:13
# %receiving:True
r.seekable()
# %sending:14
# %receiving:True
r.isatty()
# %sending:15
# %receiving:False
r.write_through
# %sending:16
# %receiving:False
