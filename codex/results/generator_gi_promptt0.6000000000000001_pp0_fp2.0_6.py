gi = (i for i in ())
# Test gi.gi_code.co_flags & CO_GENERATOR

# Try to create a generator iterator
try:
    gi = (i for i in range(5))
except TypeError:
    print("SKIP")
    raise SystemExit

# Test gi.gi_code.co_flags & CO_GENERATOR

# Try to create a generator function
try:
    def f():
        yield 1
except TypeError:
    print("SKIP")
    raise SystemExit

# Test f.__code__.co_flags & CO_GENERATOR
