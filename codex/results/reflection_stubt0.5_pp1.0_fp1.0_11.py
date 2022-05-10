fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# test_builtin_code_co_consts
def f(): pass
code = f.__code__
code.co_consts = (1, 2, 3)
code.co_consts

# test_builtin_code_co_consts_immutable
def f(): pass
code = f.__code__
code.co_consts = (1, 2, 3)
code.co_consts

# test_builtin_code_co_filename
def f(): pass
code = f.__code__
code.co_filename = "foo.py"
code.co_filename

# test_builtin_code_co_firstlineno
def f(): pass
code = f.__code__
code.co_firstlineno = 10
code.co_firstlineno

# test_builtin_code_co_flags
def f(): pass
code = f.__code__
code.co_flags = 0
code.co_flags

# test_builtin_code_co_freevars
def f():
