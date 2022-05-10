import types
# Test types.FunctionType
def test_types_FunctionType():
    """
    >>> test_types_FunctionType()
    True
    """
    def f(): pass
    return type(f) is types.FunctionType

# Test types.LambdaType
def test_types_LambdaType():
    """
    >>> test_types_LambdaType()
    True
    """
    f = lambda: None
    return type(f) is types.LambdaType

# Test types.GeneratorType
def test_types_GeneratorType():
    """
    >>> test_types_GeneratorType()
    True
    """
    def f():
        yield
    return type(f()) is types.GeneratorType

# Test types.BuiltinFunctionType
def test_types_BuiltinFunctionType():
    """
    >>> test_types_BuiltinFunctionType()
    True
    """
    return type(len) is types.BuiltinFunctionType

# Test types.BuiltinMethodType
def test_types_BuiltinMethodType():
    """
    >>> test_types
