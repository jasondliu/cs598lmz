import types
# Test types.FunctionType, types.LambdaType, types.MethodType
# (copied from test_types)
def test_types():
    def f(): pass
    assert type(f) is types.FunctionType
    assert type(lambda x: x) is types.LambdaType
    assert type(f.__code__) is types.CodeType
    assert type(f.__code__.co_code) is types.StringType
    assert type(f.__code__.co_consts) is types.TupleType
    assert type(f.__code__.co_varnames) is types.TupleType
    assert type(f.__code__.co_freevars) is types.TupleType
    assert type(f.__code__.co_cellvars) is types.TupleType
    assert type(iter(f.__code__.co_cellvars)) is types.IteratorType
    assert type(iter(f.__code__.co_cellvars).next) is types.FunctionType
    assert type(f.__code__.co_filename)
