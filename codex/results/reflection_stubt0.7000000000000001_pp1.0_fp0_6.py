fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn.__code__.co_argcount = {gi}
""")
    # This test is skipped if it fails to compile the above code.
    with raises(TypeError) as excinfo:
        fn()
    assert "co_argcount must be an integer" in str(excinfo.value)


def test_code_co_stacksize():
    import sys
    fn, mod, ns = compile_fn("""\
def fn():
    return 1 + 1
fn.__code__ = fn.__code__.__new__(fn.__code__.__class__)
fn.__code__.co_stacksize = sys.maxsize
""")
    # This test is skipped if it fails to compile the above code.
    with raises(OverflowError) as excinfo:
        fn()
    assert "stacksize too big" in str(excinfo.value)

    fn, mod, ns = compile_fn("""\
def fn():
    return 1 + 1
fn.__code__ = fn.__code__.__new__(fn.
