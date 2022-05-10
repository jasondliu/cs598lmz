fn = lambda: None
# Test fn.__code__
code = testfn.__code__
code is not None
code.co_name == 'testfn'
code.co_filename == __file__
code.co_firstlineno == inspect.currentframe().f_lineno - 1
code.co_argcount == 0
code.co_flags == (67 | inspect.CO_NOFREE)
code.co_consts == ()
code.co_varnames == ()
code.co_cellvars == ()
code.co_freevars == ()
code.co_stacksize == 1
code.co_code == b'd\x00Z\x00j\x01|\x00d\x01\x17\x00S\x00'
code.co_lnotab == b'\x01\x00'
code.__sizeof__() >= 61

# Test fn.__code__.__eq__ and fn.__code__.__ne__.
c1 = testfn.__code__
c2 = testfn.__code__
c1 is c2
c1 == c2
c
