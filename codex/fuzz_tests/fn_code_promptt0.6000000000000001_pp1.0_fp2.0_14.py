fn = lambda: None
# Test fn.__code__.co_filename
# Test fn.__code__.co_firstlineno

# Test fn.__code__.co_varnames
# Test fn.__code__.co_argcount

# Test fn.__code__.co_cellvars
# Test fn.__code__.co_freevars

# Test fn.__code__.co_flags
# Test fn.__code__.co_consts

# Test fn.__code__.co_lnotab

def test_code_new():
    def f():
        pass
    old_code = f.__code__
    new_code = code.CodeType(
        old_code.co_argcount,
        old_code.co_nlocals,
        old_code.co_stacksize,
        old_code.co_flags,
        old_code.co_code,
        old_code.co_consts,
        old_code.co_names,
        old_code.co_varnames,
        old_code.co_filename,
       
