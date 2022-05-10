import weakref
# Test weakref.ref(object)

class C(object):
    pass

c = C()
r = weakref.ref(c)
assert r() is c

class D(object):
    def __init__(self):
        self.c = C()

d = D()
r = weakref.ref(d.c)
assert r() is d.c

# Test weakref.ref(object, callback)

class C(object):
    pass

c = C()
l = []
def callback(arg):
    l.append(arg)
r = weakref.ref(c, callback)
assert r() is c
del c
collect()
assert l == [r]

class D(object):
    def __init__(self):
        self.c = C()

d = D()
l = []
def callback(arg):
    l.append(arg)
r = weakref.ref(d.c, callback)
assert r() is d.c
del d
collect()
assert l == [r]

# Test weakref.proxy(
