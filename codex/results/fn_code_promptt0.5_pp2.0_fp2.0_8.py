fn = lambda: None
# Test fn.__code__.co_varnames

# Test fn.__code__.co_argcount

# Test fn.__code__.co_cellvars

# Test fn.__code__.co_filename

# Test fn.__code__.co_firstlineno

# Test fn.__code__.co_flags

# Test fn.__code__.co_freevars

# Test fn.__code__.co_lnotab

# Test fn.__code__.co_name

# Test fn.__code__.co_names

# Test fn.__code__.co_nlocals

# Test fn.__code__.co_stacksize

# Test fn.__code__.co_consts

# Test fn.__code__.co_code


class TestCode(object):
    def test_co_varnames(self):
        def f():
            pass

        assert f.__code__.co_varnames == ()

    def test_co_argcount(self):
        def f():
            pass


