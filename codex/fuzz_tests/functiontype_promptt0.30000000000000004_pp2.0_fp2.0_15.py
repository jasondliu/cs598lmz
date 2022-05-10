import types
# Test types.FunctionType
def test_types_FunctionType():
    assert types.FunctionType(lambda x: x, globals(), 'foo')

# Test types.LambdaType
def test_types_LambdaType():
    assert types.LambdaType(lambda x: x, globals(), 'foo')

# Test types.GeneratorType
def test_types_GeneratorType():
    assert types.GeneratorType(lambda: (yield))

# Test types.CodeType
def test_types_CodeType():
    assert types.CodeType(0, 0, 0, 0, '', (), (), (), '', '', 0, '')

# Test types.TracebackType
def test_types_TracebackType():
    try:
        1/0
    except Exception as e:
        tb = e.__traceback__
        assert types.TracebackType(tb.tb_frame, tb.tb_lasti, tb.tb_lineno, tb.tb_next)

# Test types.FrameType
def test_types
