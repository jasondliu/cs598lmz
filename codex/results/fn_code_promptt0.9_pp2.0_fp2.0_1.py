fn = lambda: None
# Test fn.__code__ == fn.__call__.__code__ is False
def fn_gen(): return fn_gen
fn_gen().__Code__ = fn_gen().__call__.__code__
fn_gen.__code__ = fn.__code__
fn_gen.__code__ == fn.__code__
fn_gen().__code__ == fn.__code__
fn_gen.__code__ == fn_gen().__code__

# eval and exec arg
# --------------------------------------

eval({}, {})
eval({}, {}, {})
eval({}, {}, {})

# exec
exec('print(1)')
exec('print(1)', {})
exec('print(1)', {}, {})

# raise doesn't take an exception instance or tuple as an argument
# --------------------------------------

# Issue #3632: As of 3.3, "raise X" and "raise X()" always raise
# an exception instance or class, but never a tuple.
raise ValueError
raise ValueError()
try:
    raise ValueError, None
except TypeError:
    pass
try
