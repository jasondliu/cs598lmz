fn = lambda: None
# Test fn.__code__.__init__
f = fn.__code__.__init__
# Test fn.__code__.__new__
f = fn.__code__.__new__


def check_globals_binary(fn):
    fn()
    check_module_globals(fn.__globals__)


def check_module_globals(mod_globals):
    for name in mod_globals:
        assert_not_isinstance(mod_globals[name], types.ModuleType)


def test_code_labels():
    def f(x):
        a = 1
        b = 1
        if x:
            a = 2
            b = 2
            return a
        else:
            a = 3
            b = 3
            return b

    assert f(1) == 2
    assert f(0) == 3

    # Test co_lnotab
    def g(x):
        a = 1
        b = 1
        # Jump over the first comparison
        while True:
            a = 3
            b =
