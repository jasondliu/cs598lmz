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

b"A" + view
view.release()

if False:
    import gc
    gc.collect()
    gc.collect()
    import inspect
    ref = inspect.getargvalues(inspect.stack()[0][0])[3]["ref"]
    del ref
    view = None
    bytesize = None
    ffi_str = None
    gc.collect()
    gc.collect()
    gc.collect()
    del gc
    del inspect
    del ref
    del view
    del bytesize
    del ffi_str
    del gc
