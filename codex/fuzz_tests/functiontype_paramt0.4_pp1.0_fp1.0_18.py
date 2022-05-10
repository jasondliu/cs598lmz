from types import FunctionType
list(FunctionType(f.__code__, globals(), "f"))

#%%
from types import FunctionType

def curry(f, *a):
    def curried(*more):
        return f(*(a + more))
    return curried

def compose(f, g):
    def composed(*args, **kwargs):
        return f(g(*args, **kwargs))
    return composed

def trace(tag):
    def traced(f):
        def traced_f(*args, **kwargs):
            print(tag, args, kwargs)
            result = f(*args, **kwargs)
            print(tag, "->", result)
            return result
        return traced_f
    return traced

def double(x):
    return 2 * x

double = trace("double")(double)

def square(x):
    return x * x

square = trace("square")(square)

def sum_squares_double(x, y):
    return sum(map(double, [square(x), square(y)]))

sum_squares
