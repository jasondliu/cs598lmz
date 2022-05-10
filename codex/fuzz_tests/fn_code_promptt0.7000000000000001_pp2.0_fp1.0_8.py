fn = lambda: None
# Test fn.__code__.co_argcount
__test_fn.__code__.co_argcount = 3
__test_fn.__code__.co_nlocals = 3
__test_fn.__code__.co_varnames = ('a', 'b', 'c')
__test_fn.__code__.co_varnames = ('a', 'b', 'c')
__test_fn.__code__.co_cellvars = ('a', 'b')
__test_fn.__code__.co_freevars = ('d', 'e')
__test_fn.__code__.co_code = b'\x01\x0a\x00\x00\x02\x0a\x00\x00\x02\x0a\x00\x00\x00'
# Test fn.__code__.co_flags
# Test fn.__code__.co_flags & CO_VARARGS
__a = __b = __c = 3
__test_fn.__code__.co_argcount = 0
__test_fn =
