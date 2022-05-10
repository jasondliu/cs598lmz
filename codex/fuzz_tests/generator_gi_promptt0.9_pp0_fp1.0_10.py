gi = (i for i in ())
# Test gi.gi_code


class G():

    def f(self):
        pass  # in __class__ scope


g = G()
assert g.f.__class__ is types.MethodType
assert g.f.__class__.__name__ == 'method'
assert g.f.__class__.__module__ in ('types', 'builtins')
assert g.f.__class__.__code__ is G.f.__code__
assert g.f.__class__.__dict__ is G.f.__dict__
assert g.f.__class__.__bases__ == (object,)


def tail_call_optimized(arg):
    """Python does not really support TCO, but this is a good approximation
    for testing purposes."""
    global f_n
    f_n = 0
    try:
        return f(arg)
    except RuntimeError:
        return f_n


def f(n):
    global f_n
    f_n = f_n+1
    if n <= 1:
        return 1
    return f(n - 1
