fn = lambda: None
gi = (i for i in ())
fn.__code__ = fn.__code__.__class__()
gi.gi_code = gi.gi_code.__class__()
fn()
next(gi)

# Issue #11863: crash when a code object is created with a NULL co_consts
# pointer.
import types
code = types.CodeType(0, 0, 0, 0, 0, b'', (), (), (), '', '', 0, b'')

# Issue #12353: crash when a code object is created with a NULL co_names
# pointer.
code = types.CodeType(0, 0, 0, 0, 0, b'', (), (), (), '', '', 0, b'', ())

# Issue #12353: crash when a code object is created with a NULL co_varnames
# pointer.
code = types.CodeType(0, 0, 0, 0, 0, b'', (), (), (), '', '', 0, b'', (), ())

# Issue #12353: crash when a code object is created with a NULL co_freevars
# pointer.
code = types.CodeType(
