import weakref
# Test weakref.ref with one argument
#
# This test was added to check SF bug #249977.

class C:
    pass

o = C()
r = weakref.ref(o)

if not hasattr(r(), '__class__'):
    print 'r() has no __class__ attribute'
elif r().__class__ != C:
    print 'r() has the wrong class'

print 'ok'
