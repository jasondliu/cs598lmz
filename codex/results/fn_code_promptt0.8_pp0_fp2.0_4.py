fn = lambda: None
# Test fn.__code__.co_flags & 0xC
del fn

# Used by unittests/test_tools.py
# Test fn.__code__.co_names is not None
def fn(): pass
# Test fn.__code__.co_names is not None
del fn

# Used by unittests/test_tools.py
# Test fn.__code__.co_varnames is not None
def fn(a): pass
# Test fn.__code__.co_varnames is not None
del fn

# Used by unittests/test_tools.py
# Test fn.__code__.co_stacksize, fn.__code__.co_code, fn.__code__.co_consts,
# fn.__code__.co_lnotab
def fn(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x,
       y, z, aa=1, bb=2, cc=3
