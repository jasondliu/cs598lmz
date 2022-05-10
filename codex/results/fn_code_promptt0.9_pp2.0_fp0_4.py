fn = lambda: None
# Test fn.__code__
def test_Code():
    co = fn.__code__
    assert type(co) is types.CodeType
    assert type(co.co_argcount) is int
    #assert type(co.co_cellvars) is str
    assert type(co.co_code) is str
    assert type(co.co_consts) is tuple
    assert type(co.co_filename) is str
    assert type(co.co_firstlineno) is int
    #assert type(co.co_flags) is int
    #assert type(co.co_freevars) is str
    assert type(co.co_lnotab) is str
    assert type(co.co_name) is str
    assert type(co.co_names) is tuple
    assert type(co.co_nlocals) is int
    assert type(co.co_stacksize) is int
    #assert type(co.co_varnames) is str

# Test fn.__defaults__
def test_Defaults():
    assert type(fn.__default
