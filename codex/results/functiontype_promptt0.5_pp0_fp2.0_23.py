import types
# Test types.FunctionType
def test_types_FunctionType():
    assert types.FunctionType is type(lambda: None)

# Test types.LambdaType
def test_types_LambdaType():
    assert types.LambdaType is type(lambda: None)

# Test types.CodeType
def test_types_CodeType():
    def f(): pass
    assert types.CodeType is type(f.__code__)

# Test types.TracebackType
def test_types_TracebackType():
    try:
        1/0
    except ZeroDivisionError:
        import sys
        tb = sys.exc_info()[2]
        assert types.TracebackType is type(tb)
        assert tb.tb_frame is sys._getframe()
        assert tb.tb_lasti == tb.tb_frame.f_lasti
        assert tb.tb_lineno == tb.tb_frame.f_lineno

# Test types.FrameType
def test_types_FrameType():
    import sys
