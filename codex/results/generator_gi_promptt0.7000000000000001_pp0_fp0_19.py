gi = (i for i in ())
# Test gi.gi_code.co_name
i = gi.gi_code.co_name

# Test that a generator object is an instance of GeneratorType and
# GeneratorType is a subclass of object.
assert(isinstance(gi, GeneratorType))
assert(issubclass(GeneratorType, object))

# Test that we can call next() on the generator and get the appropriate
# StopIteration exception.
try:
    i = next(gi)
except StopIteration as e:
    i = e.value
assert(i == 1)

# Test that we can iterate over the generator and it will raise a
# StopIteration exception.
def sum_generator(n):
    s = 0
    for i in range(n):
        s += i
        yield i
    yield s

s = 0
for i in sum_generator(10):
    s += i
assert(s == 45)

# Test that we can catch the StopIteration exception and get the last
# value from the generator.
try:
    for i in sum_generator(10):
        pass
except
