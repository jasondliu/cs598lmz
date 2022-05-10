import weakref
# Test weakref.ref for new style classes

class C(object):
    pass

c = C()
r = weakref.ref(c)
c.x = r

