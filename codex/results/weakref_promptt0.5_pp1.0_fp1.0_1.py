import weakref
# Test weakref.ref() with a class instance

class Foo:
    pass

f = Foo()
wr = weakref.ref(f)
assert wr() is f

class Bar:
    def __init__(self):
        self.x = 42
        self.y = "hello"
        self.z = [1, 2, 3]

b = Bar()
wr = weakref.ref(b)
assert wr() is b
assert wr().x == 42
assert wr().y == "hello"
assert wr().z == [1, 2, 3]

class Foo:
    def __init__(self, x):
        self.x = x

f = Foo("hello")
wr = weakref.ref(f)
assert wr().x == "hello"
f.x = 42
assert wr().x == 42

class Foo:
    pass

f = Foo()
wr = weakref.ref(f)
del f
try:
    wr()
except:
    pass
else:
    raise Exception("expected exception")

class Foo:
    def __init__(
