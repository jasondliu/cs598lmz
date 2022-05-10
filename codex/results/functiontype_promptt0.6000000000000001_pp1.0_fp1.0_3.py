import types
# Test types.FunctionType
class C:
    def f(self):
        return "hello"

def method(self):
    return "world"

class D(object):
    def f(self):
        return "hello"

def method(self):
    return "world"

class E(object):
    @staticmethod
    def f(self):
        return "hello"

def method(self):
    return "world"


def test_function_type():
    def f():
        return "hello"
    assert isinstance(f, types.FunctionType)
    a = types.FunctionType(f.func_code, {})
    assert a() == "hello"
    b = types.FunctionType(f.func_code, {}, "foo")
    assert b.func_name == "foo"
    c = types.FunctionType(f.func_code, {}, "foo", ("a", "b"))
    assert c.func_defaults == ("a", "b")
    d = types.FunctionType(f.func_code, {}, "foo", (),
