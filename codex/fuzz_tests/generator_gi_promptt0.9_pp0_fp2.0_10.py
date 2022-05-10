gi = (i for i in ())
# Test gi.gi_code does not exist.
try:
    gi.gi_code
except AttributeError:
    print('SKIP')
    raise SystemExit

# Create a generator function to check gi_code
def gen():
    yield 1
    yield 2

g = gen()

# Test that gi_code is a code object
print(type(g.gi_code))

# Test that we get a ReferenceError when it is set
try:
    g.gi_code = "foo"
except ReferenceError:
    print('ReferenceError')
