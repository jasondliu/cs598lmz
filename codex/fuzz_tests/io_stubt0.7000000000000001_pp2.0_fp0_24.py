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

# __weakref__ should be set to None
print(view.__array_interface__['__weakref__'])
del view
gc.collect()

# Check that weakref is really dead
import sys
if sys.getrefcount(object()) == 2:
    print('OK')
else:
    print('BUG!')
