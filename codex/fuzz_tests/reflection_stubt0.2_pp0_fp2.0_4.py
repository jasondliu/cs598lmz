fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# Issue #17098: test that the code object of a function created by
# types.FunctionType() is not a generator.
def f():
    pass

assert not isinstance(f.__code__, types.GeneratorType)

# Issue #17098: test that the code object of a function created by
# types.FunctionType() is not a generator.
def f():
    pass

assert not isinstance(f.__code__, types.GeneratorType)

# Issue #17098: test that the code object of a function created by
# types.FunctionType() is not a generator.
def f():
    pass

assert not isinstance(f.__code__, types.GeneratorType)

# Issue #17098: test that the code object of a function created by
# types.FunctionType() is not a generator.
def f():
    pass

assert not isinstance(f.__code__, types.GeneratorType)

# Issue #17098: test that the code object of a function created by
# types
