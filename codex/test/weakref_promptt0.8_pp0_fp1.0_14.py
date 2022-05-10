import weakref
# Test weakref.ref on a class instance
class Foo:
    def __init__(self):
        self.x = 100
    def method(self):
        pass

F = Foo()
wr = weakref.ref(F)
assert wr().x == 100
del F
wc = weakref.ref(wr)
assert wc()() is None
assert wc()() is None
del wc

# getweakrefcount:
class Foo:
    def __init__(self):
        self.x = 100
    def method(self):
        pass

class Bar:
    pass

x = Foo()
y = Foo()
z = Bar()

wc = weakref.getweakrefcount
assert wc(z) == 0
assert wc(y) == 1
assert wc(x) == 1
assert wc(z) == 0
del y
assert wc(x) == 1
assert wc(z) == 0

# getweakrefs (pending)
xx = Foo()
