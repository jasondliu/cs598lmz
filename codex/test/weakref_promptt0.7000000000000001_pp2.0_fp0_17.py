import weakref
# Test weakref.ref(...) is callable
ref = weakref.ref(3.14)


class Foo:
    def __init__(self, x):
        self.x = x


class Bar:
    def __init__(self, x):
        self.x = x


# Test weakref.WeakKeyDictionary(...)
d = weakref.WeakKeyDictionary({Foo(3): 1})
# Test weakref.WeakKeyDictionary[...]
_ = d[Foo(3)]
# Test weakref.WeakKeyDictionary[...] assignment
d[Foo(3)] = 2
# Test weakref.WeakKeyDictionary[]
_ = d[Foo(4)]
# Test weakref.WeakKeyDictionary del
del d[Foo(4)]
# Test weakref.WeakKeyDictionary in
_ = Foo(4) in d
# Test weakref.WeakKeyDictionary len
_ = len(d)
# Test weakref.WeakKeyDictionary iter
for _ in d:
    pass
# Test weakref.WeakKeyDictionary bool
