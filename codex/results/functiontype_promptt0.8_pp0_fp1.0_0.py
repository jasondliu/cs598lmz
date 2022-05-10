import types
# Test types.FunctionType
def f(): pass
x = types.FunctionType(f.func_code, f.func_globals)
assert x() == None
# Test types.BuiltinFunctionType
x = types.BuiltinFunctionType(range)
assert x(5) == [0, 1, 2, 3, 4]

# test types.LambdaType
x = types.LambdaType(lambda: 111, {}, '')
assert x() == 111

a = '123'
assert type(a) == str
assert type(a) != bytes

# Issue #3182
y = {'__doc__': 'stuff'}
assert type('', (), y) == type
assert type(123) == int


# Test type.__qualname__

assert int.__qualname__ == 'int'
assert bytes.__qualname__ == 'bytes'
assert str.__qualname__ == 'str'
assert bool.__qualname__ == 'bool'
assert type.__qualname__ == 'type'

class A:
    def foo():
        pass
assert A.
