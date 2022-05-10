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

# Test that the buffer is released when the file is closed.
gc.collect()

def callback():
    global callback_called
    callback_called = True

weakref.finalize(view, callback)
del view
gc.collect()
assert callback_called
