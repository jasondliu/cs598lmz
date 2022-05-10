fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# The following is a regression test for a bug in the bytecode optimizer.
# The bug was that the optimizer was not properly handling the
# LOAD_GLOBAL opcode when the global name was not a string.
# The following code used to raise a TypeError.

def f():
    def g():
        return x
    x = 1
    return g

f()()

# The following is a regression test for a bug in the bytecode optimizer.
# The bug was that the optimizer was not properly handling the
# LOAD_GLOBAL opcode when the global name was a string that was not
# interned.  The following code used to raise a TypeError.

def f():
    def g():
        return x
    x = 1
    return g

f()()

# The following is a regression test for a bug in the bytecode optimizer.
# The bug was that the optimizer was not properly handling the
# LOAD_GLOBAL opcode when the global name was a string that was not
# interned.  The following
