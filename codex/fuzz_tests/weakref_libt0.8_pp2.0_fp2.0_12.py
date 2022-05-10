import weakref


class Foo:
    pass

a = Foo()
print(a)
wr = weakref.ref(a)
print(wr)
print(wr())

del a
print(wr)
print(wr())
