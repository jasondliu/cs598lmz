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

view[0] = 10

# import warnings
# warnings.simplefilter('error', ResourceWarning)

def callback(obj):
    print('callback')
    raise Exception

weakref.ref(obj, callback)

del obj

import gc
gc.collect()

print('OK')
