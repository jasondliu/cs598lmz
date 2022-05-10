import weakref
# Test weakref.ref() for a function.
def f():
    pass
r = weakref.ref(f)
assert r() is f
# Test weakref.ref() for a built-in function.
r = weakref.ref(len)
assert r() is len
# Test weakref.ref() for a built-in method.
r = weakref.ref(''.join)
assert r() is ''.join
# Test weakref.ref() for a class.
class C:
    pass
r = weakref.ref(C)
assert r() is C
# Test weakref.ref() for an instance.
o = C()
r = weakref.ref(o)
assert r() is o
# Test weakref.proxy() for a function.
p = weakref.proxy(f)
assert p is f
# Test weakref.proxy() for a built-in function.
p = weakref.proxy(len)
assert p is len
# Test weakref.proxy() for a built-in method.
p = weakref.proxy(''.join)
assert p is ''.join
# Test weak
