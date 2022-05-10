import types
# Test types.FunctionType

def test_types_FunctionType():
    assert types.FunctionType(lambda: None, {}, "foo", (), ())

# Test types.LambdaType

def test_types_LambdaType():
    assert types.LambdaType(lambda: None, {}, "foo", (), ())

# Test types.GeneratorType

def test_types_GeneratorType():
    assert types.GeneratorType(lambda: None, {}, "foo", (), ())

# Test types.CodeType

def test_types_CodeType():
    assert types.CodeType(0, {}, (), (), (), (), (), (), "", "", 0, "")

# Test types.TracebackType

def test_types_TracebackType():
    try:
        1/0
    except:
        tb = sys.exc_info()[2]
        assert types.TracebackType(tb.tb_frame, tb.tb_lasti, tb.tb_lineno, tb.tb_next)

# Test types.
