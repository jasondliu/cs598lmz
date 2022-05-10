import types
# Test types.FunctionType
def test_types_functiontype():
    assert types.FunctionType(lambda: 0, globals())

# Test types.MethodType
def test_types_methodtype():
    assert types.MethodType(lambda self: self, None, None)

# Test types.BuiltinFunctionType
def test_types_builtinfunctiontype():
    assert types.BuiltinFunctionType(lambda: 0)

# Test types.BuiltinMethodType
def test_types_builtinmethodtype():
    assert types.BuiltinMethodType(lambda self: self, None)

# Test types.ModuleType
def test_types_moduletype():
    assert types.ModuleType('test_types_moduletype')

# Test types.TracebackType
def test_types_tracebacktype():
    assert types.TracebackType(None, None, None)

# Test types.FrameType
def test_types_frametype():
    assert types.FrameType(None, None, None)

# Test types.CodeType
def test_types_codetype():
    assert types.Code
