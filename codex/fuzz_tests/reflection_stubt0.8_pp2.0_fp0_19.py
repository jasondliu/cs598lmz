fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi
fn()  # TypeError: expected code object, generator found
# but the right way to test is "if type(code) == types.CodeType",
# not "if isinstance(code, type(lambda: None))"
# because the latter would raise TypeError

# test pure function with closure (custom python-style function)
# pure function with closure is not supported yet


def f(x):
    def g(y):
        return x + y
    return g


@myjit
def jitf(x):
    def jitg(y):
        return x + y
    return jitg


assert f(1)(2) == jitf(1)(2)


# test for correct exception for invalid input (custom python-style function)
# FunctionGraph cannot match the two function definitions,
# because the two function definitions have same func_name.
# The two function definitions should have different func_name.
# Therefore, the def should be moved in the test function.
def jitf_bad(x):
    def jitg(y):
        return x
