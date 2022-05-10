gi = (i for i in ())
# Test gi.gi_code and gi.gi_frame

def g(a):
    yield a + 1

def f(a, b):
    c = yield a + b
    yield c + 1
    yield c + 2
    return a * b * c

def h():
    return (yield from f(1, 2))

gf = g(1)
ff = f(1, 2)
hf = h()

try:
    gf.send(None)
except TypeError:
    print("SKIP")
    raise SystemExit

assert gf.gi_code.co_name == "g"
assert gf.gi_frame.f_code.co_name == "g"
assert gf.gi_frame.f_back is None
assert ff.gi_code.co_name == "f"
assert ff.gi_frame.f_code.co_name == "f"
assert ff.gi_frame.f_back is None
assert hf.gi_code.co_name == "h"
assert hf.gi_frame.f_code
