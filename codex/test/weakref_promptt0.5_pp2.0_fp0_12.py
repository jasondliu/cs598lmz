import weakref
# Test weakref.ref()

def f():
    pass

w = weakref.ref(f)

assert w() is f

assert w() is f

class C:
    pass

w = weakref.ref(C)

assert w() is C

assert w() is C

class C:
    pass

w = weakref.ref(C())

assert w() is C

assert w() is C

class C:
    pass

w = weakref.ref(C())

assert w() is C

assert w() is C

class C:
    pass

w = weakref.ref(C())

assert w() is C

assert w() is C

class C:
    pass

w = weakref.ref(C())

assert w() is C

assert w() is C

class C:
    pass

w = weakref.ref(C())

assert w() is C

assert w() is C

class C:
    pass

w = weakref.ref(C())

assert w
