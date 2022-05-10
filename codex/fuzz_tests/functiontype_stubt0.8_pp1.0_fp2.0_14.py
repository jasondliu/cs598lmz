from types import FunctionType
a = (x for x in [1])
b = FunctionType(a.gi_frame.f_code, a.gi_frame.f_globals, 'b', (), a.gi_frame.f_closure)
print(a.gi_frame.f_code)
print(a.gi_frame.f_code.co_freevars)
print(b([2]))

# a generator function
def generator_function(n):

    # iterating over a range
    # of values
    for i in range(n):
        # yielding the square
        # of the number
        yield i ** 2

# generator object
generator_object = generator_function(3)
print(type(generator_object))

for value in generator_object:
    print(value)


# a generator function
def generator_function():
    for i in range(10):
        yield i

# generator object
generator_object = generator_function()
print(type(generator_object))


print(generator_object.gi_running)
print(next(generator_object))
print(gener
