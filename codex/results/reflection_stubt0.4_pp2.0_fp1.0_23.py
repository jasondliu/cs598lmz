fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #24804: In PyEval_EvalFrameEx, when the frame's f_lasti is -1,
# it should be set to f_code->co_firstlineno.
def f():
    pass
f.__code__.co_firstlineno = -1
f()

# Issue #24801: In PyEval_EvalFrameEx, when the frame's f_lasti is -1,
# it should be set to f_code->co_firstlineno.
def f():
    pass
f.__code__.co_firstlineno = 1
f.__code__.co_lnotab = b"\x00\x00"
f.__code__.co_varnames = ()
f()

# Issue #24804: In PyEval_EvalFrameEx, when the frame's f_lasti is -1,
# it should be set to f_code->co_firstlineno.
def f():
    pass
f.__code__.co_firstlineno = 1
f.
