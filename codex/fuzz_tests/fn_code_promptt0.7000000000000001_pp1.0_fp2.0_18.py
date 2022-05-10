fn = lambda: None
# Test fn.__code__.co_name.
# We do this in a function because globals() is not a dictproxy and
# therefore setting __code__.co_name will not work.
def fn():
    pass
def test_func_name():
    assert fn.__name__ == 'fn'

# Test fn.__code__.co_filename.
def test_func_file():
    assert fn.__code__.co_filename == __file__

# Test fn.__code__.co_firstlineno.
def test_func_line():
    assert fn.__code__.co_firstlineno == fn.__code__.co_firstlineno

def test_set_code_filename_and_line():
    def f():
        return
    f.__code__ = types.CodeType(0, 0, 0, 0, 0, b'', (), (), (), '', '<string>',
                                10, b'', (), (), ())
    assert f.__code__.co_filename == '<string>'
    assert f.__code__.co_firstlineno
