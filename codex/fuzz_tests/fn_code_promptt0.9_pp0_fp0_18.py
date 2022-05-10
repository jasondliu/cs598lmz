fn = lambda: None
# Test fn.__code__.co_argcount
def test_fn(argcount):
    return id(fn.__code__.co_argcount) == id(argcount)

assert fn.__code__.co_varnames == None
fn.__code__.co_varnames = ()
assert fn.__code__.co_varnames == ()
try:
    fn.__code__.co_varnames = (1, 2)
except TypeError:
    assert True
else:
    assert False

assert fn.__code__.co_consts == None
fn.__code__.co_consts = ()
assert fn.__code__.co_consts == ()
try:
    fn.__code__.co_consts = (1, 2)
except TypeError:
    assert True
else:
    assert False

assert fn.__code__.co_names == None
fn.__code__.co_names = ()
assert fn.__code__.co_names == ()
fn.__code__.co_names = ('x', 'y')

