import types
# Test types.FunctionType, which is a special type.
class cls(object):
    def __init__(self, value):
        self.value = value
    def __call__(self, other):
        return cls(self.value + other)

def test_function_type():
    # The fact that builtin function can have attributes is a mistake and this
    # test acts more like a warning to prevent further mistakes.
    def f():
        pass
    assert type(f) is types.FunctionType
    assert f.__name__ == 'f'
    assert f.__module__ == __name__
    assert f.__annotations__ == {}
    #
    def g(x: 1) -> 2:
        return int(x)
    assert g.__annotations__ == {'x': 1, 'return': 2}
    #
    assert cls('hello')(' world').value == 'hello world'

def test_silly_attributes():
    top = types.SimpleNamespace()
    a = types.SimpleNamespace(b = types.SimpleNamespace(top =
