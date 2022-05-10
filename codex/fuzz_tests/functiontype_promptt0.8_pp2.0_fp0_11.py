import types
# Test types.FunctionType wrapper
def a(): pass
def b(x): pass
def c(x,y): pass
def d(x=None): pass
def nocall(*args): pass

def test_types_callable():
    for f in [a,b,c,d,nocall]:
        assert types.FunctionType.is_callable(f)

def test_types_callable_types():
    for t in [types.FunctionType, types.BuiltinFunctionType]:
        assert t.is_callable(lambda: None)

def test_types_callable_noncallable():
    for x in [2, 2.0, "", (), [], {}]:
        assert not types.FunctionType.is_callable(x)

def test_types_callable_class():
    class C(object):
        def __call__(self):
            pass
    assert types.FunctionType.is_callable(C)

def test_types_callable_instance():
    class C(object):
        def __call__(self):
            pass
   
