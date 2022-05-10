import types
# Test types.FunctionType
def f(): pass
class C(object):
    def g(): pass
    @classmethod
    def h(cls): pass
    @staticmethod
    def i(): pass
    def j(a): pass
    def j(a, b): pass
    def j(a, b, c): pass

def test():
    assert type(f) is types.FunctionType
    assert type(C.g) is types.FunctionType
    assert type(C.h) is types.FunctionType
    assert type(C.i) is types.FunctionType
    assert type(C.j) is types.FunctionType
    assert type(next) is types.BuiltinFunctionType
    assert type(len) is types.BuiltinFunctionType
    assert type(type) is types.BuiltinFunctionType
    assert type(sys.exit) is types.BuiltinFunctionType
    assert type(test) is types.FunctionType

def test_import():
    mod1 = __import__('exceptions')
    mod2 = __import__('exceptions', globals(), locals())
    assert mod
