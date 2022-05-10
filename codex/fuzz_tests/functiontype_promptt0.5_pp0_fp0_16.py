import types
# Test types.FunctionType
def func():
    pass
print(type(func)==types.FunctionType)
print(type(abs)==types.BuiltinFunctionType)
print(type(lambda x: x)==types.LambdaType)
print(type((x for x in range(10)))==types.GeneratorType)

# Test types.StringType
print(type('abc')==types.StringType)
print(type(u'abc')==types.UnicodeType)

# Test types.BooleanType
print(type(True)==types.BooleanType)

# Test types.NoneType
print(type(None)==types.NoneType)

# Test types.IntType
print(type(1)==types.IntType)

# Test types.FloatType
print(type(1.0)==types.FloatType)

# Test types.ListType
print(type([])==types.ListType)

# Test types.TupleType
print(type(())==types.TupleType)

# Test types.DictType
print(type({
