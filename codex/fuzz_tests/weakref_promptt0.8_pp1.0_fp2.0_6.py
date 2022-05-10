import weakref
# Test weakref.ref(some_object)
a = 1
a_ref = weakref.ref(a)
print(a_ref)  # <weakref at 0x10356e5a8; to 'int' at 0x103542678>

# Test weakref.ref.__call__(a_ref)
print(a_ref())  # 1

# Test weakref.ref(some_object) enforces no circular reference
# with some_object.__weakref__
a.__weakref__ = a_ref
a_ref()  # 1
a_ref()  # 1

 
# Test weakref.ref(some_object) enforces no circular reference
# with object.__class__.__weakref__
class A(object):
    pass

a = A()  # __weakref__ is unset
a_ref = weakref.ref(a)
print(a_ref)  # <weakref at 0x10357e6c8; to 'A' at 0x10357e7b0>
a.__class__.__weakref__ = a
