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
<code>b'\x02\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\\x02\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00\\x02\x00\x00\x00\x02\x00\x00\x00\x01\x00\x00\x00'
</code>
I can't find what's going on in the source code, but this is probably only a bug in Python 3.7.0, and will be fixed in the next versions.

