import weakref
# Test weakref.ref(a) == weakref.ref(a)

class A(object):
    pass

a = A()
b = A()

print weakref.ref(a) == weakref.ref(a)  # True
print weakref.ref(a) == weakref.ref(b)  # False
# Test that the original object can be garbage collected

class A(object):
    pass

a = A()
r = weakref.ref(a)

del a
gc.collect()
print r()  # None
# Test that the original object can be garbage collected

class A(object):
    pass

a = A()
r = weakref.ref(a)

del a
gc.collect()
print r()  # None
# Test that the original object can be garbage collected

class A(object):
    pass

a = A()
r = weakref.ref(a)

del a
gc.collect()
print r()  # None
# Test that the original object can be garbage collected

class A(object):
    pass


