from types import FunctionType
list(FunctionType(f.__code__, f.__globals__, "foo", f.__defaults__, f.__closure__).__closure__)

# https://stackoverflow.com/questions/8951020/python-closures-and-nested-functions
def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier

# Multiplier of 3
times3 = make_multiplier_of(3)

# Multiplier of 5
times5 = make_multiplier_of(5)

# Output: 27
print(times3(9))

# Output: 15
print(times5(3))

# Output: 30
print(times5(times3(2)))

# https://stackoverflow.com/questions/233673/lexical-closures-in-python
def make_adder(n):
    def inner(x):
        return x + n
    return inner

add3 = make_adder(3)
add5 = make_adder(5)


