fn = lambda: None
# Test fn.__code__ without reporting a warning about calling
# _getframe().  Avoid blockage in the do_test() function defined
# below.
def test():
    global test_fn

    def f():
        def g():
            return test_fn()
        test_fn = g
    f()

test()

# Verify that g is code-like, but not a code itself.
# This used to crash, since the guard variable in f said it was
# returning a function, but g wasn't one.
c = test_fn.__code__
print(isinstance(c, types.CodeType), c.co_name, c.co_firstlineno,
      c.co_flags & (constants.CO_NEWLOCALS | constants.CO_OPTIMIZED |
                    constants.CO_VARARGS | constants.CO_VARKEYWORDS |
                    constants.CO_NESTED | constants.CO_GENERATOR |
                    constants.CO_NOFREE | constants.CO_COROUTINE |
                    constants.CO_ITERABLE_COROUTINE))

c = test
