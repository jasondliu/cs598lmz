fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #23691: A function with an empty bytecode sequence should not
# crash the interpreter.
def f():
    pass
f.__code__ = type(f.__code__)(0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')
f()

# Issue #23691: A function with a NULL bytecode sequence should not
# crash the interpreter.
def f():
    pass
f.__code__ = type(f.__code__)(0, 0, 0, 0, None, (), (), (), '', '', 0, b'')
f()

# Issue #23691: A function with a non-empty bytecode sequence should
# crash the interpreter.
def f():
    pass
f.__code__ = type(f.__code__)(0, 0, 0, 0, b'\x00', (), (), (), '', '', 0, b'')
try:
    f()
except ValueError:
    pass
else:
    raise Exception("didn't raise")

# Issue #23691
