gi = (i for i in ())
# Test gi.gi_code.co_flags
# (note: we could also use f_locals.values() to get the generator object,
# but this would only work after the first yield, and would also grab any
# other generator objects created in the same scope)
def f():
    yield 42
print(f().gi_code.co_flags & 0x20)
# Test gi.gi_running
def f():
    g = (i for i in ())
    yield 42
    yield g.gi_running
    yield sys._getframe(0).f_lasti == -1
print(list(f()))
# Test gi.gi_frame
def f():
    g = (i for i in ())
    yield 42
    yield g.gi_frame is sys._getframe(0)
    yield sys._getframe(0).f_lasti == -1
print(list(f()))
# Test gi.gi_yieldfrom
def f():
    g = (i for i in ())
    yield 42
    yield g.gi_yieldfrom is None
print(list(f()
