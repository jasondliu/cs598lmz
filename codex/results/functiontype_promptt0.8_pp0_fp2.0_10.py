import types
# Test types.FunctionType
def func(x, y, z=1):
    """Return the average of x and y (and z if present)."""
    if z==1:
        return (x + y)/2.0
    else:
        return (x + y + z)/3.0
print(type(func))
print(func)
print(func(3, 4))
print(func(3, 4, 5))

# Test types.LambdaType
total = lambda x, y: x + y
print(total(1, 4))

# Test types.GeneratorType
def fib(n):
    """Return n Fibonacci numbers."""
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b

f = fib(10)
print(type(f))
print(next(f))
print(next(f))
print(next(f))
print(next(f))

# Test types.GeneratorType

def permutations(seq):
    """Generate permutations of the sequence seq.
