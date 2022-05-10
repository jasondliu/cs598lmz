gi = (i for i in ())
# Test gi.gi_code in local scope.
gi.gi_code.__name__
gi.gi_code.__scope__
gi.gi_code.__annotations__
gi.gi_code.__kwdefaults__

def f(a, b, c):
    yield a
    yield b
    yield c
    pass

fi = f(1, 2, 3)

# Test fi.gi_code in closure scope.
fi.gi_code.__name__
fi.gi_code.__scope__
fi.gi_code.__annotations__
fi.gi_code.__kwdefaults__

def f():
    y = yield 10
    return y

fi = f()
d = fi.send(None)
try:
    res = fi.send(12)
except StopIteration as e:
    res = e.value

res == 12

def f():
    y = yield from range(3)
    return y
fi = f()
fi.send(None)
try:
    res = fi.send(12)
except StopIteration as e
