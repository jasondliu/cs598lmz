import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect():
print('Testing gc.collect() with "pass"')
weakref_list = []

def check_wref(wref):
    print('check_wref(%r):' % (wref,))

class TestObject:
    def __init__(self):
        print('In TestObject.__init__()')
    def __del__(self):
        print('In TestObject.__del__()')

def TestFunc():
    obj = TestObject()
    ref = weakref.ref(obj, check_wref)
    weakref_list.append(ref)
    print('TestFunc: obj=%s' % obj)
    print('TestFunc: ref=%s' % ref)
    del obj
    return

print('Calling TestFunc()')
TestFunc()
for ref in weakref_list:
    print('For loop: unwrapped reference=%r' % ref())

gc.collect()
for ref in weakref_list:
    print('For loop after gc.collect(): unwrapped reference
