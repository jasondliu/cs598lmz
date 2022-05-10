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
r.fileno()
# %sending:18
# Traceback:
#    File "<stdin>", line 1, in <module>
# io.UnsupportedOperation: fileno
r.flush()
# %sending:19
r.read(2)
# %sending:20
# %receiving:sp
r.read()
# %sending:21
# %receiving:am

class MyIO(io.IOBase):
    def close(self):
        return super().close()


My
