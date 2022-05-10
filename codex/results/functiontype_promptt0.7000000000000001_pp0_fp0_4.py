import types
# Test types.FunctionType -- should return True
def f(): pass
def g(): pass
def h(): pass
types.FunctionType(f.__code__, {})
types.FunctionType(g.__code__, {}, "foo")
types.FunctionType(h.__code__, {}, "foo")
types.FunctionType(h.__code__, {}, "foo", (1, 2))
types.FunctionType(h.__code__, {}, "foo", None, 123)

# Test types.MethodType -- should return True
import types
class C:
    def __init__(self, a):
        self.a = a
    def foo(self):
        pass

types.MethodType(C.foo, C(1))
types.MethodType(C.foo, C(1), C)
types.MethodType(C.foo, C(1), C, C)

def test_types():
    # Test that types.FunctionType and types.MethodType are accepted as is
    # (i.e. no error message).
    def f(): pass
    def g(): pass
