fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_getattr_recursion
class A:
    def __getattr__(self, attr):
        return getattr(self, attr)

a = A()
a.a

# test_getitem_recursion
class A:
    def __getitem__(self, item):
        return self[item]

a = A()
a[0]

# test_getslice_recursion
class A:
    def __getitem__(self, item):
        return self[item]

a = A()
a[0:1]

# test_getstate_recursion
class A:
    def __getstate__(self):
        return self.__dict__

a = A()
a.__getstate__()

# test_hash_recursion
class A:
    def __hash__(self):
        return hash(self)

a = A()
hash(a)

# test_init_recursion
class A:
    def __init__(self):
        self
