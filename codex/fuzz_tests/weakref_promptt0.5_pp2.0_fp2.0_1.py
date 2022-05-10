import weakref
# Test weakref.ref
#
import gc

class Dummy:
    pass

a = Dummy()
b = Dummy()

w = weakref.ref(a)

print w(), w() is a, w() is b

a = None

print gc.collect()
print w(), w() is a, w() is b

print w() == None, w() is None
print w() is None

print w() == a, w() is a

print w() == b, w() is b

print w() == w(), w() is w()

b = None

print gc.collect()
print w(), w() is a, w() is b

print w() == None, w() is None
print w() is None

print w() == a, w() is a

print w() == b, w() is b

print w() == w(), w() is w()

# Test weakref.proxy
#
a = Dummy()
b = Dummy()
c = Dummy()

w = weakref.proxy(a)

