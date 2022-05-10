import types
# Test types.FunctionType

def type_test1():
    return types.FunctionType

def type_test2():
    return types.FunctionType(lambda x: x, {})

def type_test3():
    return types.FunctionType(lambda x: x, {})("hello")

def type_test4():
    return types.FunctionType(lambda x: x, {}, "hello")

def type_test5():
    return types.FunctionType(lambda x: x, {}, "hello", ("x",))

def type_test6():
    return types.FunctionType(lambda x: x, {}, "hello", ("x",), {})

def type_test7():
    return types.FunctionType(lambda x: x, {}, "hello", (), {})

def type_test8():
    return types.FunctionType(lambda x: x, {})("hello", "world")

def type_test9():
    return types.FunctionType(lambda x: x, {}, "hello", (), {})("hello", "world")


# Test types.BuiltinFunctionType
