import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect() equivalence.
assert gc.collect() == gc.collect(2)
# Test ability to enable weakref callbacks.
def callback(r):
    global saw_callback
    saw_callback = 1
r = weakref.ref(CallbackClass(), callback)
t = Win32Test()
wref = weakref.ref(t)
del t
gc.collect()
assert saw_callback


# Testing file(x).close()
def test_runfile(fn):
    print 'executing', fn
    execfile(fn)

if __name__ == '__main__':
    test_runfile('filebug.py')
