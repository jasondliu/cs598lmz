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
gc.collect()

import gc; gc.collect()
print(view[0] == 1)
</code>
This appears to be enough to trigger the crash in my unpatched Python, but not on a patched one.

