import types
# Test types.FunctionType
def foo(): return 1
def bar(x,y): return x # return None
def baz(x,y): return x,y
f = foo
b = bar
z = baz
assert type(f) is types.FunctionType
assert type(b) is types.FunctionType
assert type(z) is types.FunctionType
assert foo is f
assert bar is b
assert baz is z
assert not foo is bar
assert not foo is baz
assert not bar is baz
assert not bar is foo
assert not baz is foo
assert not baz is bar
r = f()
assert r == 1
r = b(1,2)
assert r == 1
r = z(1,2)
assert r[0] == 1
assert r[1] == 2


# Test types.GeneratorType
def gen():
    yield 1
    yield 2
    yield 3
g = gen()
assert type(g) is types.GeneratorType
assert g.gi_frame.f_lasti == -1
i = next(g)
assert i == 1
assert g
