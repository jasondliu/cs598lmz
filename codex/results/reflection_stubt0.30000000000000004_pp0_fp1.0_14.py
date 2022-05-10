fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()

# This should raise a TypeError, but instead it raises a SystemError.
# The problem is that the code object is not a code object, but a
# generator.  The code object is created by the code generator, which
# is a generator, and the code object is yielded by the code generator.
# The code object is then passed to the function object, which is
# created by the function generator.  The function generator yields
# the function object, which is then returned by the function
# generator.  The function object is then called.  When the function
# object is called, it calls the code object, which is a generator,
# and the generator is executed.  When the generator is executed, it
# yields the code object, which is then returned by the function
# object.  The code object is then called.  When the code object is
# called, it calls the code object, which is a generator, and the
# generator is executed.  When the generator is executed, it yields
# the code object, which is then returned by the code object.  The
# code object is then called.  When the
