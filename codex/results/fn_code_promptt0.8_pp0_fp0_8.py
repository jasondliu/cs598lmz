fn = lambda: None
# Test fn.__code__.co_argcount
test_fn.__code__ = test_fn.func_code = test_fn.func_closure = fn
assert test_fn.__code__.co_argcount == 2

# Test fn.__code__.co_varnames
def test2_fn(a, b, c, d, e, f, g, h, i, j, k, l, m, n, o, p, q, r, s, t, u, v, w, x, y, z):
    pass

test2_fn.__code__ = fn
assert test2_fn.__code__.co_varnames == (
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
)

# Test fn.__code__.co_filename
test_fn.__
