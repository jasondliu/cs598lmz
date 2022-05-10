fn = lambda: None
# Test fn.__code__ is OK, and restore fn.__code__ after returning
def with_test_code(code, fn):
    code_was = fn.__code__
    fn.__code__ = code
    try:
        yield fn
    finally:
        fn.__code__ = code_was

# Same, but also ensures fn.__code__.co_freevars is OK, and restores it, too
def with_test_cellvars(code, fn):
    code_was = fn.__code__
    fn.__code__ = code
    cellvars = code.co_freevars
    try:
        yield fn
    finally:
        fn.__code__ = code_was

# Add or override a var in fn.__code__.co_freevars
def with_cellvar(code, name, val):
    code_was = code.co_freevars
    cellvars = list(code_was) + [name]
    code.co_freevars = tuple(cellvars)
    setattr(fn, name, val)
   
