import types
# Test types.FunctionType
def f():
    pass
f()
def g():
    f()
g()
def f():
    g()
f()
# Test types.MethodType
class Foo:
    def f():
        pass
    def g():
        f()
    def h():
        g()
        Foo.f()
Foo.f()
Foo.g()
Foo.h()
x = Foo()
#x.f()
#x.g()
#x.h()
# Test types.TypeType
class Bar:
    pass

class Foo:
    def f():
        pass
    def g():
        f()
    def h():
        g()
        Foo.f()
        Foo()
        Foo()()
        Bar()
        Bar
        Bar()()
        Baz()
        Baz
        Baz()()

Foo.f()
Foo.g()
Foo.h()
x = Foo()
#x.f()
#x.g()
#x.h()
class Baz:
    pass

# Test type(
