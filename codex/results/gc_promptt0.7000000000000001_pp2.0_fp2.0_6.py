import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class Foo:
    pass

def callback(x):
    print 'callback for', x

f = Foo()
w = weakref.ref(f, callback)
print 'callback after', w()

gc.collect()
print 'callback after', w()

f = None
gc.collect()
print 'callback after', w()

gc.collect()

# Test gc.garbage

class Foo:
    pass

f = Foo()
f.f = f
w = weakref.ref(f)
gc.garbage.append(f)
f = None

gc.collect()

print w() is None

print
print 'done'
print
print 'now testing'
print 'http://www.python.org/sf/495079'
print 'http://www.python.org/sf/495080'
print 'http://www.python.org/sf/495081'
print 'http://www.python.org/sf/495082'
print

class A:
    pass

class B(object):
