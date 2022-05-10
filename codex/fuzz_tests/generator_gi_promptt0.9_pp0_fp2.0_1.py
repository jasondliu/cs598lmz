gi = (i for i in ())
# Test gi.gi_code
def f(): yield 1
assert f().gi_code == f.__code__

# Test gi_frame
def g(n):
    for i in range(3):
        yield n
    def h():
        for i in range(4):
            yield n
        for i in g(n+1):
            yield i
    for i in h():
        yield i

it = g(1)
for i in range(3):
    assert it.gi_frame.f_locals['n'] == 1
    next(it)

assert it.gi_frame.f_locals['n'] == 1
assert it.gi_frame.f_code.co_name == 'h'

for i in range(4):
    assert it.gi_frame.f_locals['n'] == 1
    next(it)

assert it.gi_frame.f_locals['n'] == 2
for i in range(3):
    assert it.gi_frame.f_locals['n'] == 2
    next(it)

assert it.
