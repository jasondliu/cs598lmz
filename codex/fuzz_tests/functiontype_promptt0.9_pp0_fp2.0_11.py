import types
# Test types.FunctionType


def test_function_type():
    assert types.FunctionType is types.BuiltinFunctionType


def test_tuple_assign_bug():
    d = {}
    TUP = types.TupleType
    X = 'a',
    Y = TUP(X)
    d[X] = 1
    assert d[Y] == 1
    assert Y == X

# Test types.NoneType


def test_none_type():
    raises(TypeError, id, None)
    raises(TypeError, hash, None)
    raises(TypeError, bool, None)
    raises(TypeError, str, None)

# Test types.ObjectType


def test_obj_type():
    class OldStyle:
        pass
    a = OldStyle()
    assert type(a) is types.InstanceType
    raises(TypeError, types.ObjectType)
    raises(TypeError, type, a)

# Test types.LambdaType


def test_lambda_type():
    raises(SyntaxError, eval, 'lambda: 0')


