gi = (i for i in ())
# Test gi.gi_code is None, and gi.gi_frame is None.
gi.gi_code  # PYVER: 2.x
gi.gi_frame  # PYVER: 2.x

# Check that a generator with a yield raises a TypeError when called
def f():
    yield 1
try:
    f()
except TypeError:
    print("TypeError")

# Check that a generator with a yield raises a TypeError when called
# via a class's __call__ method.
class C:
    def __call__(self):
        yield 1
try:
    c = C()
    c()
except TypeError:
    print("TypeError")

# Check that a generator with a yield raises a TypeError when called
# via a class's __call__ method.
class C:
    def __call__(self):
        yield 1
try:
    c = C()
    c()
except TypeError:
    print("TypeError")

# Check that a generator with a yield raises a TypeError when called
# via a class's __call__ method.
class C:
