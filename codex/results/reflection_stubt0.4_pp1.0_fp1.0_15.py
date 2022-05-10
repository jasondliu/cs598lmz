fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
"""
    result, output = test(code, '<string>')
    assert result == 0
    assert output == 'Traceback (most recent call last):\n' \
                     '  File "<string>", line 1, in <module>\n' \
                     'TypeError: code object can\'t be a generator\n'


def test_non_code_object_in_code():
    code = """def fn():
    fn.__code__ = None
    fn()
"""
    result, output = test(code, '<string>')
    assert result == 0
    assert output == 'Traceback (most recent call last):\n' \
                     '  File "<string>", line 2, in fn\n' \
                     'TypeError: fn() takes 0 positional arguments but 1 was given\n'


def test_non_code_object_in_function():
    code = """def fn():
    pass
fn.__code__ = None
fn()
"""
    result, output = test(code, '<string>')
   
