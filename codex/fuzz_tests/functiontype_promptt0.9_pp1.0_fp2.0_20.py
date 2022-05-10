import types
# Test types.FunctionType type, check __class__ in the type test.
print(type(g) is types.FunctionType)
# Test types.MethodType type, check __class__ in the type test.
print(type(_a.f) is types.MethodType)
# Test types.ClassType type, check __class__ in the type test.
print(type(A) is types.ClassType)
# Test _types.InstanceType type, check __class__ in the type test.
print(type(_a) is _types.InstanceType)
# Test types.TupleType type, check __class__ in the type test.
print(type((1, 2)) is types.TupleType)
# Test types.ListType type, check __class__ in the type test.
print(type([1, 2]) is types.ListType)
# Test types.DictType type, check __class__ in the type test.
print(type({1: 2}) is types.DictType)
# Test types.SliceType type, check __class__ in the type test.
print(type(slice(1, 2, 3
