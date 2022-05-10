import weakref
# Test weakref.ref (add_cleanup()
# Currently only tests it as a weakref callback.
class X:
    pass
x = X()
r = weakref.ref(x, lambda _: None)
# Test weakref.ref.__repr__ method
r = weakref.ref(x, lambda _: None)
r.__repr__()
r = weakref.ref(x, lambda _: None)
r.__str__()
r = weakref.ref(x, lambda _: None)
len(r.__str__()) == len(r.__repr__())
# Test weakref.getweakrefcount
aw = weakref.ref(x, lambda _: None)
bw = weakref.ref(x, lambda _: None)
cw = weakref.ref(x, lambda _: None)
dw = weakref.ref(x, lambda _: None)
weakref.getweakrefcount(x)
# Test weakref.getweakrefs
aw = weakref.ref(x, lambda _: None)
bw = weakref.ref(
