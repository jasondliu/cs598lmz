fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code
fn.__name__ = "foo"
fn.__qualname__ = "bar"
fn.__annotations__ = {"a": 1}
fn.__dict__ = {"a": 2}
fn.__module__ = "baz"
fn.__defaults__ = (1, 2, 3)
fn.__kwdefaults__ = {"a": 1, "b": 2}
fn.__closure__ = (1, 2, 3)
fn.__globals__ = {"a": 1, "b": 2}
fn.__get__ = lambda: None
fn.__set__ = lambda: None
fn.__delete__ = lambda: None

# Test __new__
class A:
    def __new__(cls):
        return object.__new__(cls)

a = A()

# Test __init__
class B:
    def __init__(self):
        self.a = 1
        self.b = 2
        self.c = 3

b = B()

# Test __del__
class
