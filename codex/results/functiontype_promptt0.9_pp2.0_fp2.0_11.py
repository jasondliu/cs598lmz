import types
# Test types.FunctionType to be <type 'function'>

def test_type():
    assert type(types.FunctionType("foo")) == types.FunctionType

def test_type_is_function():
    assert type(types.FunctionType("foo")) == types.FunctionType("foo")

def test_type_is__type_function():
    assert isinstance(types.FunctionType, type)

def test_type_object():
    assert type(type(types.FunctionType)) == type

def test_isinstance():
    def bar(): pass
    assert isinstance(type(bar), type)

def test_issubclass():
    def bar(): pass
    assert issubclass(type(bar), type)

def test_function_override():
    def foo(): pass
    class Base:
        def __call__(self):
            return "Base"
    class Derived(Base):
        def __call__(self):
            return "Derived"
    d = Derived()
    assert d() == "Derived"
    funcid = id(foo)
    foo =
