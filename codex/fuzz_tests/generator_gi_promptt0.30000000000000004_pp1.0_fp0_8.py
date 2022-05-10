gi = (i for i in ())
# Test gi.gi_code.co_varnames

def f():
    yield 1
    yield 2

def g():
    for i in f():
        yield i

gi = g()
assert gi.gi_code.co_varnames == ('i',)

# Test gi.gi_frame.f_locals

def f():
    yield 1
    yield 2

def g():
    for i in f():
        yield i

gi = g()
assert gi.gi_frame.f_locals == {'i': 1}
gi.next()
assert gi.gi_frame.f_locals == {'i': 2}

# Test gi.gi_frame.f_lasti

def f():
    yield 1
    yield 2

def g():
    for i in f():
        yield i

gi = g()
assert gi.gi_frame.f_lasti == -1
gi.next()
assert gi.gi_frame.f_lasti == 6
gi.next()
assert gi.gi_frame.
