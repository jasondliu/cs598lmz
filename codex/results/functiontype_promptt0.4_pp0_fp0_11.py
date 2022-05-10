import types
# Test types.FunctionType
def test_function_type_1():
    def f(): pass
    assert isinstance(f, types.FunctionType)

def test_function_type_2():
    def f(): pass
    assert not isinstance(f, types.BuiltinFunctionType)

def test_function_type_3():
    def f(): pass
    assert not isinstance(f, types.MethodType)

def test_function_type_4():
    def f(): pass
    assert not isinstance(f, types.LambdaType)

def test_function_type_5():
    def f(): pass
    assert not isinstance(f, types.GeneratorType)

def test_function_type_6():
    def f(): pass
    assert not isinstance(f, types.CodeType)

def test_function_type_7():
    def f(): pass
    assert not isinstance(f, types.TracebackType)

def test_function_type_8():
    def f(): pass
    assert not isinstance(f, types.FrameType)


