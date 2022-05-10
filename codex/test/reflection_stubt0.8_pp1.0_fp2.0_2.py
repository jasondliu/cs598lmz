fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code  # type: ignore
f = fn.__code__
try:
    print(f)
except TypeError:
    print("TypeError")
try:
    print(f.co_code)
except AttributeError:
    print("AttributeError")
func = eval("lambda x: x")
print(func(3))
class X:
    def foo(self):
        return "hello, world"
x = X()
print(x.foo())
pt = X.foo
print(pt.__get__(x))
class X:
    def foo(self):
        return "hello, world"
x = X()
print(X.foo.__get__(x))
print(x.foo)
class Wrapper:
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, attrname):
        print("Trace:", attrname)
        return getattr(self.wrapped, attrname)

x = Wrapper([1, 2, 3])
x
