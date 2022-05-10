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

# this is here to keep a reference to File alive to work around the CPython
# reference counting bug which would crash the interpreter when it's destructor
# is called

import itertools
itertools.count(1)
</code>

