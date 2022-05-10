import types
# Test types.FunctionType
def func():
    pass
print(type(func) == types.FunctionType)
print(type(abs) == types.BuiltinFunctionType)
print(type(lambda x: x) == types.LambdaType)
print(type((x for x in range(10))) == types.GeneratorType)

# Test types.UnicodeType
print(type('abc') == types.UnicodeType)
print(type(u'abc') == types.UnicodeType)

# Test types.StringType
print(type('abc') == types.StringType)
print(type(b'abc') == types.StringType)

# Test types.ListType
print(type([]) == types.ListType)

# Test types.DictType
print(type({}) == types.DictType)

# Test types.IntType
print(type(1) == types.IntType)

# Test types.FloatType
print(type(1.0) == types.FloatType)

# Test types.BooleanType
print(type(True) == types
