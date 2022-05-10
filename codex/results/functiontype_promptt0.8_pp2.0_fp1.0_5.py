import types
# Test types.FunctionType
for obj in [
    object(),
    object,
    object(),
    object,
    lambda x: x,
    lambda: 1,
    lambda x, y: x+y,
    lambda x, y, z: x+y+z,
    lambda **kw: kw,
    lambda x, y=1: x+y
]:
    if type(obj) is types.FunctionType:
        print(obj, "is a function object")
    else:
        print(obj, "is not a function object")
# Test types.MethodType
for obj in [
    object(),
    object,
    object(),
    object,
    lambda x: x,
    lambda: 1,
    lambda x, y: x+y,
    lambda x, y, z: x+y+z,
    lambda **kw: kw,
    lambda x, y=1: x+y
]:
    if type(obj) is types.MethodType:
        print(obj, "is a method object")
    else:
        print(obj, "is not a method
