import types
# Test types.FunctionType, function
if type(len) is types.BuiltinFunctionType:
    print('type(len) is types.BuiltinFunctionType:.\n')
# type(xxx) is int/float/bool/list/tuple/dict/set/str/frozenset/type/classobj/file/
# Superclass must be known exactly.
class MyInt(int):
    pass
if type(MyInt(10)) is int:
    print('type(MyInt(10)) is int')
# Why not use type()
print(str(type([1,2,3])),"len([1,2,3]) = ",len([1,2,3]))
