import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo(object):
    def __init__(self):
        self.l = [1, 2]

x = Foo()
x.l.append(x)

w = weakref.ref(x)
print w
print w()

del x
print w()

gc.collect()
print w()

print gc.garbage

# Cleanup
import gc
gc.collect()

# Test weakref.WeakKeyDictionary

class Foo(object):
    def __init__(self):
        self.l = [1, 2]

x = Foo()
x.l.append(x)

d = weakref.WeakKeyDictionary()
d['foo'] = x

w = weakref.ref(x)
print w
print w()

del x
print w()

gc.collect()
print w()
print d

# Cleanup
import gc
gc.collect()

# Test weakref.WeakValueDictionary

class Foo(object):
    def __init__(self):
       
