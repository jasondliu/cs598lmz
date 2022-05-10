import weakref
# Test weakref.ref(obj)

class A(object):
    pass

a = A()
wr = weakref.ref(a)
assert wr() is a

# Test weakref.ref(obj, callback)

class B(object):
    pass

b = B()
calls = []
def callback(arg):
    calls.append(arg)

wr = weakref.ref(b, callback)
assert wr() is b
del b
import gc
gc.collect()
assert calls == [wr]

# Test weakref.proxy(obj)

class C(object):
    pass

c = C()
p = weakref.proxy(c)
assert p is c

# Test weakref.proxy(obj, callback)

class D(object):
    pass

d = D()
calls = []
def callback(arg):
    calls.append(arg)

p = weakref.proxy(d, callback)
assert p is d
del d
import gc
gc.collect()
assert calls == [p]

# Test weakref.
