import types
# Test types.FunctionType
# FunctionType is the type of user-defined functions
#
# The following test is derived from test_types.py in the Python distribution.
#
def f():
    pass
try:
    f.func_code
except AttributeError:
    pass
else:
    # FunctionType is a type, but not a class
    assert type(f) == types.FunctionType
    assert type(f) != type
    assert isinstance(f, types.FunctionType)
    assert not isinstance(f, type)
    # Functions have a func_name attribute
    assert f.__name__ == 'f'
    # Functions have a func_code attribute
    assert isinstance(f.func_code, types.CodeType)
    # Functions have a func_defaults attribute
    assert f.func_defaults == None
    assert f.func_globals == globals()
    # Functions have a func_doc attribute
    assert f.__doc__ == None
    # Functions have a func_dict attribute
    assert isinstance(f.func_dict, types.DictType)


