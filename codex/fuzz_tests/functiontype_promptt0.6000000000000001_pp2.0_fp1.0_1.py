import types
# Test types.FunctionType
def test_FunctionType():
    f = lambda: None
    assert isinstance(f, types.FunctionType)

# Test types.GeneratorType
def test_GeneratorType():
    def gen():
        yield 1
        yield 2
    g = gen()
    assert isinstance(g, types.GeneratorType)

# Test types.LambdaType
def test_LambdaType():
    f = lambda: None
    assert isinstance(f, types.LambdaType)

# Test types.MappingProxyType
def test_MappingProxyType():
    d = {'a': 1, 'b': 2}
    p = types.MappingProxyType(d)
    assert isinstance(p, types.MappingProxyType)

# Test types.MethodType
def test_MethodType():
    class C:
        def f(self):
            pass
    c = C()
    m = c.f
    assert isinstance(m, types.MethodType)

# Test types.SimpleNamespace
def test_SimpleNamespace():
   
