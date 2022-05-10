fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
''')
    with assert_raises(TypeError, message='a generator cannot be a code object'):
        exec(source)

def test_func_with_code_not_a_code():
    source = py3skip("'''\nfn = lambda: None\nfn.__code__ = 'foo'\n''")
    with assert_raises(TypeError, message='__code__ must be a code object'):
        exec(source)

def test_func_with_code_co_argcount_not_int():
    source = py3skip("'''\nfn = lambda: None\nfn.__code__ = code = fn.__code__\ncode.co_argcount = 'foo'\n''")
    with assert_raises(TypeError, message='co_argcount must be an integer'):
        exec(source)

def test_func_with_code_co_argcount_negative():
    source = py3skip("'''\nfn = lambda: None\nfn.__code__ = code = fn
