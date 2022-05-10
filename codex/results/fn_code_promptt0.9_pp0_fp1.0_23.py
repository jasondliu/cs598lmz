fn = lambda: None
# Test fn.__code__.co_consts = (None,)
# Test fn.__code__.co_names = ()
# Test fn.__code__.co_varnames = ()
# Test fn.__code__.co_argcount = 0
# Test fn.__code__.co_heaponly = 1
# Test fn.__code__.co_flags = 67|1
def test13(fn):
    fn()


#
# Test functools.partial function
#
# Test partial.__code__.co_name = '<lambda>'
# Test partial.__code__.co_firstlineno = 2503
# Test partial.__code__.co_flags = 67|1
def test14(partial):
    partial()


# Test partial.__code__.co_freevars = ()
# Test partial.__closure__
# Test partial.__closure__[0].__dict__
# Test partial.__closure__[0].__dict__['cell_contents'] is len
#
# Test partial.__code__.co_code = b'|\x00
