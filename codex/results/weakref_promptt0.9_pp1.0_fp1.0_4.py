import weakref
# Test weakref.ref() with a self-referencing cycle.
class P(object):
    def __init__(self, foo, bar):
        self.foo = foo
        self.bar = bar


class C(P):

    def __init__(self, foo, bar, baz):
        super(C, self).__init__(foo, bar)
        self.baz = baz


c = C(1, 2, 3)
r = weakref.ref(c, selfref)
print(r)
del c
gc.collect()
print(r)
def selfref(r):
    pass


# Test weakref.callback() on a self-referencing cycle.
def selfref2(r):
    pass


c = C(1, 2, 3)
assert selfref2 not in weakref.getweakrefs(c)
r = weakref.ref(c, selfref2)
print(r)
del c
gc.collect()
print(r)
assert selfref2 not in weakref.getweakrefs(c)
