fn = lambda: None
# Test fn.__code__ is a code object and all attrs are writable
code = fn.__code__
code.co_argcount = 1
code.co_nlocals = 2
code.co_stacksize = 3
code.co_flags = 4
code.co_code = b'5'
code.co_consts = (6,)
code.co_names = (7,)
code.co_varnames = (8,)
code.co_filename = '9'
code.co_name = '10'
code.co_firstlineno = 11
code.co_lnotab = b'12'
code.co_freevars = (13,)
code.co_cellvars = (14,)

# Test fn.__traceback__ is a traceback object and all attrs are writable
tb = fn.__traceback__
tb.tb_next = None
tb.tb_frame = None
tb.tb_lasti = 1
tb.tb_lineno = 2
tb.tb_lineno = 3

#
