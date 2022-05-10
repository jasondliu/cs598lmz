fn = lambda: None
# Test fn.__code__
# fn.__defaults__
# fn.__closure__
# fn.__code__ = code
# fn.__defaults__ = defaults
# fn.__closure__ = closure

# Test __code__ for classes
class C:
    # C.__code__
    # C.__code__ = code
    pass

# Test __code__ for methods
class D:
    def m(self): pass
    # D.m.__code__
    # D.m.__code__ = code
    # d.m.__code__
    # d.m.__code__ = code
    # D.m.im_func.__code__
    # D.m.im_func.__code__ = code
    # d.m.im_func.__code__
    # d.m.im_func.__code__ = code

# Test __code__ for generators
def g():
    yield 1
# g.__code__
# g.gi_code

# Test __code__ for coroutines
async def a():
    return 1

