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

# That will leak the view, because the destructor of the File will
# never run, because the file object is never fully closed, because
# its _finalize_closed will never run due to this bug.
gc.collect()

# Before this Py_Finalize the output is the following:
#
# Fatal Python error: objects/fileobject.c:277: file_dealloc: Assertion `self->weakreflist == NULL' failed
#
# Afterwards, the program runs without crashes.

del view
