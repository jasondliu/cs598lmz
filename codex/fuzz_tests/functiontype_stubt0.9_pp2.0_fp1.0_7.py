from types import FunctionType
a = (x for x in [1])
a.send(None)

def test(*args, **kwargs):
    return args, kwargs
test2 = FunctionType(test.__code__, test.__globals__, 'test2', test.__defaults__)
test2(1, 2, 3)
test2.__defaults__
test.__code__.co_varnames
test2.func_code

# EXAMPLE
h0 = hash((1, 2, (2, 3), 'spam'))
h0
a = 1; b = 2; c = 3
# non-hashable grouping
def group(*args): return args
group(a, b, c)
hash(group(a, b, c))
def group(a, b, c, d=1, e=2): return a+b+c+d+e
group(a, b, c)
hash(group(a, b, c))
def group(a, b, *c): return a+b+c[0]
group(a, b, c)
hash(group(a,
