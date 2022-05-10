fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__()
'''
    out, err = assert_python_failure(code)
    # TODO: should this raise a type error?
    assert 'TypeError' in err or 'TypeError' in out


def test_code_doc():
    code = '''def fn():
    "doc"
fn.__code__.__doc__
'''
    assert_python_ok(code)


def test_code_doc_setter():
    code = '''def fn():
    "doc"
fn.__code__.__doc__ = "new doc"
fn.__code__.__doc__
'''
    assert_python_ok(code)


def test_code_doc_setter_non_string():
    code = '''def fn():
    "doc"
fn.__code__.__doc__ = None
fn.__code__.__doc__
'''
    assert_python_ok(code)


def test_code_doc_setter_bad_type():
    code = '''def fn
