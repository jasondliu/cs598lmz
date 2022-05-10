import types
# Test types.FunctionType

class Foo(object):
    pass

def f1():
    pass

class Bar(object):
    def f2(self):
        pass

def test_FunctionType():
    if is_cli:
        import System
        assert type(f1) == System.Reflection.MethodInfo
        assert type(Bar.f2) == System.Reflection.MethodInfo
        return
    
    assert type(f1) == types.FunctionType
    assert type(Bar.f2) == types.MethodType

test_FunctionType()
