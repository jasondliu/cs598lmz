fn = lambda: None
# Test fn.__code__.co_filename and __code__.co_firstlineno.
def test_fn():
    pass
    # basic test
    assert fn.__code__.co_filename == __file__
    assert fn.__code__.co_firstlineno == test_fn.__code__.co_firstlineno + 1
    # test that line numbers are not recalculated
    assert test_fn.__code__.co_firstlineno == test_fn.__code__.co_firstlineno
    # test that changing the source code changes the line numbers
    oldlineno = test_fn.__code__.co_firstlineno
    exec(test_fn.__code__, globals(), locals())
    assert test_fn.__code__.co_firstlineno != oldlineno

def test_function_co_code():
    def f():
        pass

    code = f.__code__

    assert code.co_code is not None
    assert code.co_code == b'|\x00\x00|\x01\x00\x17\x00
