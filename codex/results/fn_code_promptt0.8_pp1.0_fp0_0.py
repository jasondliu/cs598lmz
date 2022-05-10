fn = lambda: None
# Test fn.__code__ is not None, but doesn't have co_firstlineno
def test_nocode_nolineno():
    test_fn.__code__ = lambda: None
    yield raises, AttributeError, _test_first_line, test_fn

@raises(ValueError)
def test_invalid_start():
    _test_first_line(test_fn, start_lineno=-1)

@raises(ValueError)
def test_invalid_end():
    _test_first_line(test_fn, end_lineno=0)

@raises(ValueError)
def test_invalid_start_end():
    _test_first_line(test_fn, start_lineno=-1, end_lineno=0)

@raises(ValueError)
def test_end_before_start():
    _test_first_line(test_fn, start_lineno=2, end_lineno=1)

def test_start_before_end():
    assert _test_first_line(test_fn, start_lineno
