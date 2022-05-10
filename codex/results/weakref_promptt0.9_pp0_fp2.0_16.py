import weakref
# Test weakref.ref as a function.

s = "abc"

wr = weakref.ref(s)
assert wr() is s

s = None

assert wr() is None

try:
    wr()
except ReferenceError:
    pass

# Test weakref.proxy.

class Foo:
    def f(self):
        return "Foo.f"

    def g(self):
        return "Foo.g"

foo = Foo()

foo_proxy = weakref.proxy(foo)

assert foo_proxy.f() == "Foo.f"
assert foo_proxy.g() == "Foo.g"

# Test the destructor.

class Bad:
    def __del__(self):
        print("this must not happen!")
        raise Exception

foo = Bad()
wr = weakref.ref(foo)
del foo

# Test finalize.

class Finalized:
    def __del__(self):
        Finalized.deleted = True

f = Finalized()

Finalized.deleted = False

