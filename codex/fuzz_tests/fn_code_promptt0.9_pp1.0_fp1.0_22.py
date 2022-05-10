fn = lambda: None
# Test fn.__code__
fn.__code__ = 3
TestError(TypeError, fn, 0)
fn.__code__ = str
TestError(TypeError, fn, 0)
fn.__code__ = fn
TestError(TypeError, fn, 0)
del fn.__code__
def check_code(co, name, args, st, op_num, lnotab, file, cls, first_lineno, freevars=(), cellvars=()):
    for k, v in dict(co_name=name, co_argcount=args, co_code=st, co_nlocals=args,
                      co_firstlineno=first_lineno, co_stacksize=2, co_flags=0,
                      co_consts=(None,), co_names=(), co_varnames=(), co_freevars=freevars,
                      co_cellvars=cellvars).items():
        if v != getattr(co, k):
            raise TestFailed, "%s.%s != %s" % (co, k, v)
    if
