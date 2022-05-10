gi = (i for i in ())
# Test gi.gi_code.co_varnames in inspect.

# Test gi.gi_frame
import dis
import sys
def foo():
    b = yield
    print(b)
    a = yield
    print(a)
    yield
t = (i for i in foo())
f=t.gi_frame
assert dis.opmap['YIELD_VALUE'] == 86
assert f.f_lasti == dis._hasarg[dis.opname[86]]
assert f.f_code == foo.__code__
assert f.f_back.f_code == gi.gi_code

# Test co_jmagic
def bar():
    print('bar')
    yield from t
print('bar')
try:
    baz = (b for b in bar())
except NameError as e:
    assert str(e) == name_error_msg
else:
    raise RuntimeError

name_error_msg = 'name \'' + t.gi_code.co_jmagic + '\' is not defined'
