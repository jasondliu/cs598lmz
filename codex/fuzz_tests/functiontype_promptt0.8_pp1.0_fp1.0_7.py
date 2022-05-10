import types
# Test types.FunctionType

def test_types_FunctionType():
    def f():
        pass
    assert isinstance(f, types.FunctionType)

def test_types_FunctionType_lambda():
    f = lambda: None
    assert isinstance(f, types.FunctionType)

# Test types.MethodType

class C:
    def method(self):
        self.m = 42
    staticmethod = staticmethod(lambda: None)
    classmethod = classmethod(lambda cls: None)

def test_types_MethodType():
    o = C()
    m = types.MethodType(o.method, o)
    m()
    assert o.m == 42

# Test types.MethodType with a staticmethod

def test_types_MethodType_staticmethod():
    o = C()
    m = types.MethodType(C.staticmethod, o)
    m()

def test_types_MethodType_staticmethod2():
    o = C()
    m = types.MethodType(o.staticmethod, o)
    m()

# Test types
