fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()
""")


# Test the effect of optimize() on functions with a __code__ attribute
# that's not a code object.
print_test(0, """
def f(x):
    return x + 1

f.__code__ = 2
f(1)
""")


# Test that optimized functions are distinguished from non-optimized
# functions.
print_test(1, """
def f():
    return 1
f.__module__ = "module"
f.__name__ = "f"
f.__defaults__ = ()
f.__closure__ = ()
f.__doc__ = ""
f.__code__ = compile("return 1", __file__, "exec")
f.func_code = f.__code__
f.func_name = f.__name__
f.func_defaults = f.__defaults__
f.func_globals = globals()
f.func_closure = f.__closure__
f.func_doc = f.__doc__
f.func_dict = {}
f.__
