import types
# Test types.FunctionType
def test_types_FunctionType():
    import types
    assert types.FunctionType
    assert isinstance(types.FunctionType, type)
    assert issubclass(types.FunctionType, object)
    assert types.FunctionType.__name__ == 'function'
    assert types.FunctionType.__module__ == 'types'
    assert types.FunctionType.__init__
    assert types.FunctionType.__call__
    assert types.FunctionType.__getattribute__
    assert types.FunctionType.__eq__
    assert types.FunctionType.__ne__
    assert types.FunctionType.__hash__
    assert types.FunctionType.__str__
    assert types.FunctionType.__doc__
    assert types.FunctionType.__repr__
    assert types.FunctionType.__get__
    assert types.FunctionType.__set__
    assert types.FunctionType.__delete__
    assert types.FunctionType.func_code
    assert types.FunctionType.func_name
    assert types.FunctionType.func_defaults
    assert types.FunctionType.func_
