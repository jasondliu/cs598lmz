fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This is a regression test for a bug in the bytecode compiler.
# The bug was that the compiler would not properly handle the
# case where the code object of a function is replaced with
# a generator.

# The bug was triggered by the following code:

# def f():
#     pass
#
# def g():
#     f.__code__ = (i for i in ())
#
# g()
# f()

# The bug was that the bytecode compiler would emit a call to
# the function f, but the code object of f had been replaced
# with a generator.

# The bug was fixed by adding a check in the bytecode compiler
# that ensures that the code object of a function is not replaced
# with a generator.
