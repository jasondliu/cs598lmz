fn = lambda: None
# Test fn.__code__.co_filename on Python 2 and 3
if PY2:
    assert fn.func_code.co_filename == "<input>"
else:
    assert fn.__code__.co_filename == "<input>"


def test_import_error_loop(space):
    # Test code is repeated below
    w_module = space.getbuiltinmodule("test")
    w_test = space.getattr(w_module, space.wrap("raises_import_error"))
    with pytest.raises(RPythonTranslationError):
        space.call_function(w_test)
    # Second call.  Import error during translation, so we expect
    # a TranslationError now.
    with pytest.raises(RPythonTranslationError):
        space.call_function(w_test)


def test_import_error_loop_jit(space, monkeypatch):
    # Test code is repeated above and below
    monkeypatch.setattr(space, 'config', FakeConfig(translation=True, jit=True))
    w_module = space.getbuiltinmodule("test")
