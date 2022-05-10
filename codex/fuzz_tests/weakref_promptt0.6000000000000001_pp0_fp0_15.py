import weakref
# Test weakref.ref()

class C(object):
    pass

o = C()
r = weakref.ref(o)
print type(r), r() is o

class D(object):
    def __init__(self, o):
        self.o = o

d = D(o)
r = weakref.ref(d)
print type(r), r() is d

o2 = C()
r = weakref.ref(o2, lambda x: print('callback'))
print type(r), r() is o2

o2 = None
print

# Test weakref.proxy()

class C(object):
    pass

o = C()
p = weakref.proxy(o)
print type(p), p is o

class D(object):
    def __init__(self, o):
        self.o = o

d = D(o)
p = weakref.proxy(d)
print type(p), p is d

o2 = C()
p = weakref.proxy(o2, lambda x: print('callback
