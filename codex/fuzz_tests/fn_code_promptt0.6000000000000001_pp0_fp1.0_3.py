fn = lambda: None
# Test fn.__code__.co_argcount
    fn.__code__.co_argcount = 1
# Test fn.__code__.co_code
    fn.__code__.co_code = b'\x00'
# Test fn.__code__.co_consts
    fn.__code__.co_consts = (1, 2, 3)
# Test fn.__code__.co_filename
    fn.__code__.co_filename = 'foo.py'
# Test fn.__code__.co_firstlineno
    fn.__code__.co_firstlineno = 1
# Test fn.__code__.co_flags
    fn.__code__.co_flags = 1
# Test fn.__code__.co_freevars
    fn.__code__.co_freevars = ('a', 'b')
# Test fn.__code__.co_kwonlyargcount
    fn.__code__.co_kwonlyargcount = 1
# Test fn.__code__.co_lnotab
    fn.__code__.co_l
