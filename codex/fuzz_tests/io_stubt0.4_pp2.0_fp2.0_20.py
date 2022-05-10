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

# Test the case where the reference count of the view is 1.
# This is the case with the io module.
view[0] = ord('a')

# Test the case where the reference count of the view is greater than 1.
view2 = view
view2[0] = ord('b')

# Test the case where the reference count of the view is 1, but
# the underlying object has a weakref.
import weakref
view3 = weakref.proxy(view)
view3[0] = ord('c')

# Test the case where the reference count of the view is greater than 1,
# and the underlying object has a weakref.
view4 = weakref.proxy(view2)
view4[0] = ord('d')

# Test the case where the reference count of the view is 1,
# and the underlying object has a weakref, and the weakref has a callback.
def callback(x):
    global called
    called = True
view5 = weakref.proxy(view, callback)
view5[0] = ord('e')
del view5

