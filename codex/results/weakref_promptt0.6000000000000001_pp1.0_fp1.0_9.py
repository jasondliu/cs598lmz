import weakref
# Test weakref.ref(o)(), weakref.ref(o)(), ...

def f(o):
    print "f(%s)" % str(o)
    if o is not None:
        print "f(%s).__class__ is %s" % (str(o), o.__class__)

o = object()
r = weakref.ref(o, f)

print "r() is", r()
print "r() is", r()
print "r() is", r()

print

o = None
print "r() is", r()
print "r() is", r()
print "r() is", r()
print "r() is", r()

print

print "r() is", r()
print "r() is", r()
print "r() is", r()
print "r() is", r()

## f(<object object at 0x00B7A318>)
## f(<object object at 0x00B7A318>).__class__ is <type 'object'>
## r() is <object object at 0x00
