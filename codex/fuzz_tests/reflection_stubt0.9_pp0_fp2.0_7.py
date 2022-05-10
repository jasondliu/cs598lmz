fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
assert raises(RuntimeError, fn)

# Test that emulating __annotations__ works.

class CG:
    def g(self):
        pass
    f = g

# Test a simple case
def f1(a: int, *, b: list) -> tuple:
    pass
assert f1.__annotations__ == {'b': list, 'a': int, 'return': tuple}

# Test that defaults are respected
def f2(a, b=42):
    pass
assert f2.__annotations__ == {'b': 42, 'a': None}

# Test that annotation of 'self' works
class C:
    def method(self, a: int) -> type(self):
        pass
assert C.__init__.__annotations__ == {}
assert C.method.__annotations__ == {'a': int, 'self': C, 'return': C}

# Test that annotation of 'self' works with inheritance:
class D(C):
    pass
assert D.__init__.__annotations__ == {}
assert
