gi = (i for i in ())
# Test gi.gi_code is not None
gi.gi_code

# Test case for issue #18394: no __code__ attribute
def f():
    pass
print(f.__code__)

# Test case for issue #18668
# Create a generator
def gen():
    yield 1

# Change the generator by assigning to its code attribute
gen.__code__ = f.__code__

# Check that the code was properly assigned
print(gen.__code__)

# Test case for issue #19226: __code__ == __new__.__code__
class A:
    def __new__(cls):
        return super(A, cls).__new__(cls)

print(A.__code__ == A.__new__.__code__)

# Test case for issue #19237: cmp_to_key(__code__)
# Check that __code__ objects are hashable
print(hash(f.__code__))

# Check that __code__ objects can be compared
print(f.__code__ == f.__code__)
print(f
