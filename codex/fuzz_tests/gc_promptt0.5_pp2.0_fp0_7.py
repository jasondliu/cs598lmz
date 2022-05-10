import gc, weakref
gc.set_debug(gc.DEBUG_COLLECTABLE)
# Test gc.collect()

class X(object):
    def __init__(self, a):
        self.a = a
    def __del__(self):
        print "X.__del__"

class Y(object):
    def __init__(self, a):
        self.a = a
    def __del__(self):
        print "Y.__del__"

def foo(x):
    print x.a

x = X(42)
y = Y(x)
x.a = y

print gc.collect()
print gc.collect()
print gc.collect()

# Test gc.get_objects()

class A(object):
    pass

class B(A):
    pass

class C(A):
    pass

a = A()
b = B()
c = C()

lst = gc.get_objects()
assert a in lst
assert b in lst
assert c in lst

# Test gc.get_referrers()

class A(object):
    pass
