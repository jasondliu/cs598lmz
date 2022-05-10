fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should raise a TypeError.
# The code object is a generator, which is not callable.
# The exception is raised in the call to PyEval_EvalCodeEx.

# This is a regression test for issue #13897.

# The bug was that the exception was not raised.
# Instead, the interpreter loop was entered,
# and the interpreter loop was never exited.
# The interpreter loop was entered because the code object
# was a generator, and the generator was not exhausted.
# The interpreter loop was never exited because the generator
# was never exhausted.
# The generator was never exhausted because the generator
# was never iterated over.
# The generator was never iterated over because the generator
# was never called.
# The generator was never called because the generator
# was not callable.
# The generator was not callable because the generator
# was not a function.
# The generator was not a function because the generator
# was not a code object.
# The generator was not a code object because the generator
# was not a function.
# The generator was not a function
