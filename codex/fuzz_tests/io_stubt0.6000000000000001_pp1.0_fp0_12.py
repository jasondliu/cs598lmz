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
print len(view)

# Test that the weakref callback is called.
import weakref

class Test(object):
    def __init__(self):
        self.callback_called = False
    def __del__(self):
        self.callback_called = True

t = Test()
def callback(obj):
    assert obj is t
    t.callback_called = True
weakref.ref(t, callback)
del t
import gc
gc.collect()
assert t.callback_called

class Test(object):
    def __init__(self):
        self.callback_called = False
    def __del__(self):
        self.callback_called = True

t = Test()
def callback(obj):
    assert obj is t
    t.callback_called = True

weakref.ref(t, callback)
del t
import gc
gc.collect()
assert t.callback_called

# Test that the weakref callback is called even if the object is resurrected
# before being destroyed.

# This test is not executed by default to
