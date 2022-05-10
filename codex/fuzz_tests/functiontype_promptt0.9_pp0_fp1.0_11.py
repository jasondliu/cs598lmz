import types
# Test types.FunctionType(args, body, globals, defaults, closure, name, filename, lineno)
def func(x, y, z):
    return x + y + z

def testfunc():

    def cmpfunc(x, y):
        if x > y:
            return 1
        else:
            return 0

    f1 = types.FunctionType(func.func_code, {})
    assert f1(1, 2, 3) == 6

    f2 = types.FunctionType(func.func_code, {}, None, None, {})
    assert f2(1, 2, 3) == 6

    # should raise a TypeError
    raises(TypeError, types.FunctionType)

    f3 = types.FunctionType(func.func_code, {}, None, None, None, "myfunc", "myfile", 2)
    assert f3.func_name == "myfunc"
    assert f3.func_code.co_filename == "myfile"
    assert f3.func_code.co_firstlineno == 2

    # should raise a TypeError

