gi = (i for i in ())
# Test gi.gi_code.co_flags
print(gi.gi_code.co_flags & inspect.CO_COROUTINE)

# Test that gi.gi_frame is always None
print(gi.gi_frame is None)

# Test that gi.gi_running is always None
print(gi.gi_running is None)

# Test that gi.gi_yieldfrom is always None
print(gi.gi_yieldfrom is None)

# Test that gi.gi_frame is always None
# But at the end of the method gi.gi_frame is None
def f():
    yield from gi

print(f().gi_frame is None)
_ = next(f())
print(f().gi_frame is None)

# Test generator-iterator.gi_code.co_flags
def f():
    yield 42

gi = (i for i in ())
print(gi.gi_code.co_flags & inspect.CO_COROUTINE)
print(f().gi_code.co_flags & inspect.CO_COROUTINE)

# Test that
