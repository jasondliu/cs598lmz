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

import ZODB.tests.util

if hasattr(view, '__delitem__'):             # Python 2
    del view[:]
elif hasattr(view, 'tobytes'):               # Python 3
    import operator
    operator.delitem(view, slice(None))
else:                                        # Cython
    del view[:]

print(ZODB.tests.util.disconnect_all())
