fn = lambda: None
# Test fn.__code__
fn.__code__ = Disassembly()
# Test fn.__closure__
func = SomeFunction()
fn.__closure__ = (5, func)
# Test fn.__defaults__
fn.__defaults__ = (5,)
# Test fn.__dict__
fn.__dict__ = {"foo": "bar"}
# Test fn.__func__
fn.__func__ = SomeFunction
# Test fn.__globals__
fn.__globals__ = globals()
# Test fn.__module__
fn.__module__ = "the module"
# Test fn.__name__
fn.__name__ = "the name"
# Test fn.__self__
class Foo:
    def __init__(self):
        self.__class__ = 1

    def bar(self):
        self.__class__ = 2

foo = Foo()
foo.bar()

# Test fn.__text_signature__
fn.__text_signature__ = "signature"

# Test for some class objects
SomeClass.__qualname__ = "
