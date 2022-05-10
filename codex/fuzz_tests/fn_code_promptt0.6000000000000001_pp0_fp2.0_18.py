fn = lambda: None
# Test fn.__code__.co_varnames
# Test fn.__code__.co_argcount
# Test fn.__code__.co_flags
# Test fn.__code__.co_cellvars
# Test fn.__code__.co_freevars

## ---------- ##
# Test fn.__code__.co_name

def test_co_name():
    def fn():
        pass
    assert fn.__code__.co_name == 'fn'

## ---------- ##
# Test fn.__code__.co_consts

def test_co_consts():
    def fn(a):
        return a
    assert fn.__code__.co_consts == (None,)

## ---------- ##
# Test fn.__code__.co_filename

def test_co_filename():
    def fn():
        pass
    assert fn.__code__.co_filename == __file__

## ---------- ##
# Test fn.__code__.co_firstlineno

def test_co_firstlineno():
    def fn():

