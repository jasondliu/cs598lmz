fn = lambda: None
# Test fn.__code__.co_filename
def test_co_filename():
    def f(): pass
    assert f.__code__.co_filename == __file__

# Test fn.__code__.co_firstlineno
def test_co_firstlineno():
    def f(): pass
    assert f.__code__.co_firstlineno == test_co_firstlineno.__code__.co_firstlineno + 1

# Test fn.__code__.co_argcount
def test_co_argcount():
    def f(): pass
    assert f.__code__.co_argcount == 0
    def f(a): pass
    assert f.__code__.co_argcount == 1
    def f(a, b): pass
    assert f.__code__.co_argcount == 2

# Test fn.__code__.co_varnames
def test_co_varnames():
    def f(): pass
    assert f.__code__.co_varnames == ('',)
    def f(a): pass
    assert f.__code
