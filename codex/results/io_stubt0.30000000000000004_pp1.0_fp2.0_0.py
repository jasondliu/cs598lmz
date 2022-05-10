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

import gc
gc.collect()

print(view)
</code>
Output:
<code>&lt;memory at 0x7f4a4e2f4c88&gt;
</code>

