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

def f():
    return view
</code>
This uses <code>io.RawIOBase.readinto</code> to fill a buffer with the contents of a <code>BytesIO</code> object.  The buffer is a C array allocated by <code>PyObject_Malloc</code>, so it should be safe from the GC.  Then, the <code>BytesIO</code> object is destroyed, and the buffer is returned.  However, when I try to run this code, I get a segfault:
<code>$ python test.py
Segmentation fault (core dumped)
</code>
I think this is because the <code>io.BufferedReader</code> object has a reference to the <code>File</code> object, which has a reference to the buffer, so the buffer is not deleted when the <code>BytesIO</code> object is deleted.  If I change <code>File</code> to inherit from <code>io.BufferedIOBase</code>, I get a different error:
<code>$ python test.py
Fatal Python error: GC object already tracked
</code
