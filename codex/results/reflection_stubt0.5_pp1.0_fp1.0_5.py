fn = lambda: None
gi = (i for i in ())
fn.__code__ = gi.gi_code = type(gi.gi_code)()
fn.__code__.co_varnames = ('a', 'b', 'c')
fn.__code__.co_argcount = 3
try:
    fn(1, 2, 3)
    print('FAIL')
except TypeError:
    print('PASS')

try:
    fn(*(1, 2, 3))
    print('FAIL')
except TypeError:
    print('PASS')

try:
    fn(**{'a': 1, 'b': 2, 'c': 3})
    print('FAIL')
except TypeError:
    print('PASS')
