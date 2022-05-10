fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi


def test_compile_code():
    with pytest.raises(SystemError):
        compile_code(fn)


def test_compile_code_globals():
    with pytest.raises(TypeError):
        compile_code(fn, {}, "", "", False, False, "", "", "")


def test_compile_code_non_function():
    with pytest.raises(TypeError):
        compile_code(gi, {}, "", "", False, False, "", "", "")
