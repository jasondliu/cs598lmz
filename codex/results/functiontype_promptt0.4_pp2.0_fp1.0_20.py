import types
# Test types.FunctionType
def test_function_type():
    assert types.FunctionType is type(test_function_type)

# Test types.BuiltinFunctionType
def test_builtin_function_type():
    assert types.BuiltinFunctionType is type(list)

# Test types.MethodType
def test_method_type():
    assert types.MethodType is type([].append)

# Test types.BuiltinMethodType
def test_builtin_method_type():
    assert types.BuiltinMethodType is type([].index)

# Test types.ModuleType
def test_module_type():
    assert types.ModuleType is type(types)

# Test types.TracebackType
def test_traceback_type():
    try:
        raise Exception("test")
    except Exception as e:
        tb = e.__traceback__
        assert types.TracebackType is type(tb)

# Test types.FrameType
def test_frame_type():
    try:
        raise Exception("test")
    except Exception as e:
        tb = e
