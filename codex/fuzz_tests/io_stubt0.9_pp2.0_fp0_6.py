import io

class File(io.RawIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

f = io.BufferedReader(File())
f.read(1)
del f
del File
gc.collect()
assert view

del view
gc.collect()

class File(io.BufferedIOBase):
    def readinto(self, buf):
        global view
        view = buf
    def readable(self):
        return True

try:
    f = File()
except NotImplementedError:
    pass
else:
    assert f.read(1)
    del f
    del File
    gc.collect()
    assert view
    del view

# check BytesIO doesn't give access to freed memory
for buf in b'', bytes(range(5)):
    f = io.BytesIO(buf)
    del buf
    f.close()
    gc.collect()
    # don't use f.getvalue(), as this allocates a new buffer if
    # BUF_CONTIG_RO is set
    del f
    gc.collect()
    f = io.BytesIO(b'foo')
    gc.collect()
    del f
    gc.collect()

# check BufferedReader doesn
