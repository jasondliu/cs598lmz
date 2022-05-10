gi = (i for i in ())
# Test gi.gi_code
assert gi.gi_code is None

def f():
    return 1

gi = (i for i in f())
# Test gi.gi_code
assert gi.gi_code == f.__code__

gi = (i for i in (1, 2, 3))
# Test gi.gi_code
assert gi.gi_code == (lambda: (yield)).__code__

gi = (i for i in (1, 2, 3)).__iter__()
# Test gi.gi_code
assert gi.gi_code == (lambda: (yield)).__code__

gi = (i for i in (1, 2, 3)).__aiter__()
# Test gi.gi_code
assert gi.gi_code == (lambda: (yield)).__code__

gi = (i for i in (1, 2, 3)).__anext__()
# Test gi.gi_code
assert gi.gi_code == (lambda: (yield)).__code__

gi = (i for i in (1,
