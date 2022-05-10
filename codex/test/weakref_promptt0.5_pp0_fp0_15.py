import weakref
# Test weakref.ref()

def f():
    pass

r = weakref.ref(f)
r()

r = weakref.ref(f, f)
r()

r = weakref.ref(f, lambda x: None)
r()

r = weakref.ref(f, lambda x: 1)
r()

r = weakref.ref(f, lambda x: "")
r()

r = weakref.ref(f, lambda x: ())
r()

r = weakref.ref(f, lambda x: [])
r()

r = weakref.ref(f, lambda x: {})
r()

r = weakref.ref(f, lambda x: set())
r()

r = weakref.ref(f, lambda x: frozenset())
r()

r = weakref.ref(f, lambda x: object())
r()

r = weakref.ref(f, lambda x: object)
r()

r = weakref.ref(f, lambda x: int)
r()

r = weakref
