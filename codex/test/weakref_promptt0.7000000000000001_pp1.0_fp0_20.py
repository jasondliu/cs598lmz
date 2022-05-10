import weakref
# Test weakref.ref with one argument
#
# This test was added to check SF bug #249977.

class C:
    pass

o = C()
r = weakref.ref(o)

