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

import gc
gc.collect()
print(view)
</code>
This will print <code>b'\x00'</code>, because the <code>io.BufferedReader</code> object is not yet garbage collected, and so the <code>File</code> object it references is not garbage collected either.

To be clear, the above is a contrived example, but it demonstrates that it is possible for a Python object to be garbage collected and for its memory to be reused for something else, but for the object to still be reachable and thus not garbage collected.

