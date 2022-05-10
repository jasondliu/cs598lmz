gi = (i for i in ())
# Test gi.gi_code is not None
print(gi.gi_code)

# Test gi.gi_frame is not None
print(gi.gi_frame)

# Test gi.gi_running is False
print(gi.gi_running)

# Test gi.gi_yieldfrom is None
print(gi.gi_yieldfrom)

# Test gi.__name__ is 'i'
print(gi.__name__)


# Test gi.__qualname__ is 'i'
print(gi.__qualname__)


def f():
    yield

# Test f().gi_code is not None
print(f().gi_code)

# Test f().gi_frame is not None
print(f().gi_frame)

# Test f().gi_running is False
print(f().gi_running)

# Test f().gi_yieldfrom is None
print(f().gi_yieldfrom)

# Test f().__name__ is 'f'
print(f().__name__)


# Test f().__qualname__ is
