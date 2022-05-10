gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & CO_COROUTINE)
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & CO_ITERABLE_COROUTINE)
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & CO_ASYNC_GENERATOR)
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & CO_FUTURE_GENERATOR_STOP)

# Test sys.setcoroutineorigin
def g1():
    yield
def g2():
    yield from g1()
sys.setcoroutineorigin(g2(), g1(), g2())

# Test sys.setcoroutineorigin
def g1():
    yield
def g2():
    yield from g1()
sys.setcoroutineorigin(g2(), g1(), g2(), 42)

# Test sys.getcoroutineorigin
def g1():
    yield
def g2():
    yield
