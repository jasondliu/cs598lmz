import types
# Test types.FunctionType:
def foo(): pass
def bar(): pass
assert type(foo) == types.FunctionType
assert type(bar) == types.FunctionType
assert not foo is bar
assert not foo == bar

class A: pass
class B(A): pass
assert type(A) == type
assert type(B) == type
assert not A is B
assert not A == B

# __eq__ / __ne__
class C:
    def __eq__(self, other):
        return True
class D(C):
    pass
c = C()
assert c == 1 and c == 1.0 and c == "hello" and c == (None,) and c == C()
assert D() == 1 and D() == 1.0 and D() == "hello" and D() == (None,)

# Test slicing of str and tuple
s = "12345"
assert s[1:3] == "23"
assert s[-3:-1] == "34"
assert s[:-1] == "1234"
assert s[1:] == "2345"
assert s[:] == s
